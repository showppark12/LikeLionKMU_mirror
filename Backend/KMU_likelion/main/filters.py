import django_filters

from .models import Calendar, Career


class CareerFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = Career
        fields = '__all__'


class CalendarFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = Calendar
        fields = '__all__'
