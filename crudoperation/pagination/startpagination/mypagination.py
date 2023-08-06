from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size=5
class Mylimitoffsetpagination(LimitOffsetPagination):
    default_limit=5
    limit_query_param='binaylimit'
    offset_query_param='binayoffset'
    max_limit=5
class Mycursorpagination(CursorPagination):
    page_size=3
    ordering='roll'