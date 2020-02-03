from rest_framework.pagination import PageNumberPagination


class Studypagination(PageNumberPagination):
      page_size = 5


class Noticepagination(PageNumberPagination):
      page_size = 5
      
class QnApagination(PageNumberPagination):
      page_size = 5
      
class Recuitpagination(PageNumberPagination):
      page_size = 5
      
class StudyCommentpagination(PageNumberPagination):
      page_size = 3
      
class NoticeCommentpagination(PageNumberPagination):
      page_size = 3
      
class QnACommentpagination(PageNumberPagination):
      page_size = 3
      
class RecuitCommentpagination(PageNumberPagination):
      page_size = 3
