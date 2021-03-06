from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template import loader
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode
from django.views import generic

from accounts.forms import SignUpForm, ContactForm
from cu_food_reviews import settings
from meal_item_alert.models import Alert
from meal_reviews.models import Review


class GoogleLoginView(generic.TemplateView):
    template_name = 'google-login-link.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['domain'] = get_current_site(self.request)
        return context


class AlertsListView(generic.ListView):
    model = Alert
    template_name = 'account-alerts-list.html'

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        return queryset

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('login')
        return super().get(request, *args, **kwargs)


class ReviewsListView(generic.ListView):
    model = Review
    template_name = 'reviews-list.html'

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        return queryset

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('login')
        return super().get(request, *args, **kwargs)


class SignUpFormView(generic.FormView):
    template_name = 'signup.html'
    form_class = SignUpForm
    def post(self, request, *args, **kwargs):
        # if not request.user.is_authenticated:
        #     return HttpResponseForbidden()
        form = self.get_form()
        # data = form.data
        # print("data: ", data)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        # this method is called when valid form data as been posted.
        valid = super().form_valid(form)
        user_name = form.cleaned_data.get('username')
        pass_word = form.cleaned_data.get('password')
        new_user = User.objects.create_user(
            username=user_name,
            email=user_name,
            password=pass_word
        )
        new_user.is_active = False
        new_user.save()
        token = default_token_generator.make_token(new_user)
        # need to encode the user id into bytes and then decode that to string
        # so that the view can later decode the bytes and convert back to user id.
        uid = urlsafe_base64_encode(force_bytes(new_user.pk)).decode()
        # uid = new_user.id

        current_site = get_current_site(self.request)
        mail_subject = 'Activate your Cornell Food account.'
        to_email = [str(new_user.email)]
        from_email = settings.DEFAULT_FROM_EMAIL
        email_context = {
            'user': new_user,
            'domain': current_site.domain,
            'uid': uid,
            'utoken': token,
        }
        html = loader.get_template('account_activation_email_2.html')
        html_content = html.render(email_context)
        msg = EmailMultiAlternatives(
            subject=mail_subject,
            from_email=from_email,
            to=[to_email]
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return valid

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['domain'] = get_current_site(self.request)
        return context

    def get_success_url(self):
        return reverse('signup_success')

def signup_success(request):
    return render(request, template_name='signup_message.html')

# class LoginFormView(generic.FormView):
#     template_name ='login.html'
#     form_class = LoginForm
#
#     def form_valid(self, form):
#         valid = super().form_valid(form)
#         return valid
#
#     def form_invalid(self, form):
#         return super().form_invalid(form)
#
#     def get_success_url(self):
#         return reverse("location_list")


class LoginFormView(LoginView):
    template_name ='login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['domain'] = get_current_site(self.request)
        return context

class LogoutFormView(LogoutView):
    template_name = 'logout.html'


class UserActivationView(generic.TemplateView):
    template_name = 'email_verification.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            uidb64 = self.request.GET.get('uidb64')
            uid = force_text(urlsafe_base64_decode(uidb64))
            token = self.request.GET.get('token')
            # print("uid: ", uid)
            # print("token: ", token)
            user = User.objects.get(id=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
            token = ''
        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            context['message'] = 'Thank you for your email verification. You can now login to your account.'
        else:
            context['message'] = 'Failed. Email verification link is invalid!'
        return context



class ContactFormView(generic.FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    def post(self, request, *args, **kwargs):
        # if not request.user.is_authenticated:
        #     return HttpResponseForbidden()
        form = self.get_form()
        # data = form.data
        # print("data: ", data)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        # this method is called when valid form data as been posted.
        valid = super().form_valid(form)
        fullname = form.cleaned_data.get('fullname')
        content = form.cleaned_data.get('content')
        user_subject = form.cleaned_data.get('subject')
        email = form.cleaned_data.get('email')
        mail_subject = 'Cornell Food Website Contact Us Message'
        message = render_to_string('contact_email.html', {
            'fullname': fullname,
            'user_subject': user_subject,
            'user_email': email,
            'user_message': content,
        })
        # print("message: ", message)
        to_email = [settings.CONTACT_TO_EMAIL]
        # print("to_email: ", to_email)
        send_mail(
            mail_subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            to_email,
            fail_silently=False
        )
        return valid

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def get_success_url(self):
        return reverse('contact_page_success')

def contact_page_success(request):
    return render(request, template_name='contact_sucess.html')