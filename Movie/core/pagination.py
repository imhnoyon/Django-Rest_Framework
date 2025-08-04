from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

class MoviePageNumberPagination(PageNumberPagination):
    page_size=2 #per page koto gula item thakbe
    page_query_param='pg'


class MovieLimitOffsetPagination(LimitOffsetPagination):
    default_limit=2
    limit_query_param='l'
    offset_query_param='o'

class MovieCursorPagination(CursorPagination):
    page_size=2
    ordering='name'
    cursor_query_param='data'