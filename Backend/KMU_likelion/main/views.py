from django.http import Http404
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from board.models import NoticeBoard

from .filters import CalendarFilter
from .models import Calendar
from .serializers import CalendarSerializer


# Create your views here.
class CalendarViewSet(viewsets.ModelViewSet):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer
    filter_class = CalendarFilter

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            notice = NoticeBoard.objects.get(id=instance.notice_id.id)
            print("notice 객체:", notice)
            print("notice의 boolean", notice.is_valid_date)
            notice.is_valid_date = False
            notice.save()
            print("notice의 boolean", notice.is_valid_date)
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)
