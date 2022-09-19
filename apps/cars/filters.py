from django_filters import rest_framework as filters
from .models import CarsModel
class CarFilter(filters.FilterSet):

    price_gt = filters.NumberFilter(field_name='price', lookup_expr='gt')
    price_gte = filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_lt = filters.NumberFilter(field_name='price', lookup_expr='lt')
    brand_start = filters.CharFilter(field_name='brand', lookup_expr='istartswith')
    brand = filters.CharFilter(field_name='brand', lookup_expr='icontains')

    class Meta:
        model=CarsModel
        fields = ('price_gt', 'price_lt', 'brand_start')

