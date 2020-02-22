import django_filters

from .models import Calendar


class CalendarFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = Calendar
        fields = '__all__'
