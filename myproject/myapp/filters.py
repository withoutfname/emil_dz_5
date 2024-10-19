import django_filters
from django.db.models import Q
from .models import Item

class ItemFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte', label="Минимальная цена")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte', label="Максимальная цена")
    query = django_filters.CharFilter(method='filter_by_all', label='Поиск')

    class Meta:
        model = Item
        fields = ['min_price', 'max_price', 'query']

    def filter_by_all(self, queryset, name, value):
        # Проверяем, есть ли значение в поле поиска
        if value:
            # Фильтруем по имени и описанию
            queryset = queryset.filter(
                Q(name__icontains=value) | Q(description__icontains=value)
            )
        return queryset
