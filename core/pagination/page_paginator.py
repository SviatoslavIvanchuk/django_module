from rest_framework.pagination import PageNumberPagination
import math
from rest_framework.response import Response
from rest_framework import status


class PagePagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'size'

    def get_paginated_response(self, data):
        count = self.page.paginator.count
        total_page = math.ceil(count/self.get_page_size(self.request))
        return Response({
            'total_items': count,
            'total_page': total_page,
            'prev': self.get_previous_link(),
            'next': self.get_next_link(),
            'data': data
        })