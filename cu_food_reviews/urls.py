"""cu_food_reviews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.contrib.auth import views as auth_views
# auth_views.PasswordResetView
# auth_views.PasswordResetForm
# auth_views.PasswordResetConfirmView
# auth_views.PasswordResetCompleteView
# auth_views.PasswordResetDoneView
from cu_food_reviews import settings
from locations.views import LocationList, privacy_page
from meal_items.views import MealItemDetailView
from accounts.views import (
    LoginFormView,
    SignUpFormView,
    LogoutFormView,
    signup_success,
    contact_page_success,
    UserActivationView,
    ContactFormView,
    AlertsListView, ReviewsListView, GoogleLoginView)

from meal_reviews.views import ReviewFormView, meal_item_review_success, ReviewDeleteView, ReviewUpdateView
from meal_item_alert.views import meal_item_alert_success, MealItemAlertFormView, MealItemAlertDeleteView

from home.views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('locations/', LocationList.as_view(), name='location_list'),
    path('contact/', ContactFormView.as_view(), name='contact_page'),
    path('contact/success', contact_page_success, name='contact_page_success'),

    path('items/<slug:item_slug>', MealItemDetailView.as_view(), name='meal_item'),

    # reviews app
    path('items/create-review/<slug:item_slug>', ReviewFormView.as_view(), name='meal_item_review'),
    path('create-review/success', meal_item_review_success, name='meal_item_review_success'),
    path('privacy/', privacy_page, name='privacy'),
    path('reviews-list/', ReviewsListView.as_view(), name='meal_reviews_list'),
    path('reviews/<id>/delete', ReviewDeleteView.as_view(), name='review_item_delete'),
    path('reviews/<id>/update', ReviewUpdateView.as_view(), name='review_item_update'),

    # alert app
    path('items/create-alert/<slug:item_slug>', MealItemAlertFormView.as_view(), name='meal_item_alert'),
    path('create-alert/success', meal_item_alert_success, name='meal_item_alert_success'),
    path('alerts/<id>/delete', MealItemAlertDeleteView.as_view(), name='meal_item_alert_delete'),
    path('alerts-list/', AlertsListView.as_view(), name='meal_items_alert_list'),

    # allauth
    path('accounts/', include('allauth.urls')),
    path('logout/', LogoutFormView.as_view(), name='logout'),
    path('login/', GoogleLoginView.as_view(), name='login')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns