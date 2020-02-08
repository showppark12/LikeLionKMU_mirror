from rest_framework.pagination import PageNumberPagination


class Studypagination(PageNumberPagination):
      page_size = 20


class Noticepagination(PageNumberPagination):
      page_size = 20
      
class QnApagination(PageNumberPagination):
      page_size = 20
      
class Recruitpagination(PageNumberPagination):
      page_size = 20
      
class StudyCommentpagination(PageNumberPagination):
      page_size = 20
      
class NoticeCommentpagination(PageNumberPagination):
      page_size = 20
      
class QnACommentpagination(PageNumberPagination):
      page_size = 20
      
class RecruitCommentpagination(PageNumberPagination):
      page_size = 20
