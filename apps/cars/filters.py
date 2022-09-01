from django.db.models import QuerySet
from rest_framework.request import Request

filters = (
    ('year', 'year'),
    ('year_lt', 'year__lt'),
    ('year_lte', 'year__lte'),
    ('year_gt', 'year__gt'),
    ('year_gte', 'year__gte'),

    ('price', 'price'),
    ('price_lt', 'price__lt'),
    ('price_lte', 'price__lte'),
    ('price_gt', 'price__gt'),
    ('price_gte', 'price__gte'),

    ('brand', 'brand__icontains')
)


def params_filter(qs: QuerySet, request: Request) -> QuerySet:
    params = request.query_params
    for key, query in filters:
        if key in params:
            qs = qs.filter(**{query: params.get(key)})
    return qs