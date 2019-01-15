from datetime import timedelta, date
from django.db.models import Avg
from django.db.models import Count
from django.shortcuts import render
from django.views.generic import ListView

from locations.models import Location
from meal_categories.models import MealCategory
from meal_events.models import MealEvent
from meal_items.models import MealItem


class LocationList(ListView):
    model = Location
    template_name = 'location-list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        today = self.request.GET.get('date', date.today().isoformat())
        open_today = self.request.GET.get('open_today')


        location_qs = self.get_queryset().prefetch_related('operatinghour_set', 'operatinghour_set__mealevent_set')
        event_qs = MealEvent.objects.filter(operating_hour__date=today).select_related('operating_hour', 'operating_hour__location')
        category_qs = MealCategory.objects.all().select_related('meal_event')
        item_qs = MealItem.objects.all(
        ).order_by('name').prefetch_related(
            'meal_category',
            'meal_category__meal_event',
            'review_set'
        ).select_related(
            'meal_location',
        ).annotate(
            rating_count=Count('review'),
            avg_rating=Avg('review__rating')
        )

        object_list_new = []
        for location in location_qs:
            location_info = self.build_location_data(location, event_qs, category_qs, item_qs, open_today)
            if location_info: object_list_new.append(location_info)

        context['object_list'] = object_list_new
        context['date_list'] = [( date.today() + timedelta(days=i) ).isoformat() for i in range(7)]
        return context

    def build_location_data(self, location, event_qs=None, category_qs=None, item_qs=None, open_today='on'):
        """
        Given a location, this method builds the location info for it.
        :return: A list
        """
        info = {
            'location': location,
            'location_data': [],
            'dining_items': [],
        }
        meal_events = [event for event in event_qs if event.operating_hour.location == location]

        if open_today == 'on' and len(meal_events) == 0: return None # skip location that is closed today

        for event in meal_events:
            meal_categories = [category for category in category_qs if category.meal_event == event]
            meal_category_data = self.build_location_category_data(location, event, meal_categories, item_qs)

            data = {
                'event': event,
                'meal_category_data': meal_category_data
            }
            info['location_data'].append(data)

            dining_items = []
            for meal_item in item_qs:
                if meal_item.meal_location == location and meal_item.is_dining_item == True:
                    dining_items.append(meal_item)
            info['dining_items'] = dining_items

        return info

    def build_location_category_data(self, location, event=None, meal_categories=None, item_qs=None):
        """
        For a given location. Build the meal category data for it.
        :return: a list
        """
        meal_category_data = []
        for category in meal_categories:
            data = {
                'category': category,
                'category_items': []
            }
            for meal_item in item_qs:
                category_qs = meal_item.meal_category.all()
                if meal_item.meal_location == location:
                    for c in category_qs:
                        if c.meal_event == event and c == category:
                            data['category_items'].append(meal_item)
                            break

            meal_category_data.append(data)
        return meal_category_data


    def get_queryset(self):
        # queryset of the location model
        query = super().get_queryset().order_by('-eatery_name')
        area_name = self.request.GET.get('campus_area_short', 'All') # Choosing All as default when nothing is provided
        if area_name == 'All': return query
        query = query.filter(campus_area_short__icontains=area_name)
        return query


def privacy_page(request):
    return render(request, template_name='privacy.html')






