import django_filters
from .models import *
from django_filters import filters

class UserFilter(django_filters.rest_framework.FilterSet):
    
    class Meta:
        model = User
        exclude=['img']
        fields='__all__'

class StudyGroupFilter(django_filters.rest_framework.FilterSet):
    group_name = filters.NumberFilter(field_name="name__id")
    class Meta:
        
        model = StudyGroup
        exclude=['img']
        fields='__all__'

class PortfolioFilter(django_filters.rest_framework.FilterSet):
   
    class Meta:
        model = Portfolio
        fields='__all__'

class Group_UserFilter(django_filters.rest_framework.FilterSet):
   
    class Meta:
        model = Group_User
        fields='__all__'

class MentoringFilter(django_filters.rest_framework.FilterSet):
   
    class Meta:
        model = Mentoring
        fields='__all__'
