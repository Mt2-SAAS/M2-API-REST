"""
    Pagination Class
"""
from rest_framework.pagination import PageNumberPagination

class RankinPageNumber(PageNumberPagination):
	page_size = 20
