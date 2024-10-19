from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Item
from django_filters.views import FilterView
from .filters import ItemFilter

class ItemListView(FilterView, ListView):
    model = Item
    template_name = 'item_list.html'
    filterset_class = ItemFilter  # Указываем класс фильтра
    context_object_name = 'items'  # Имя контекста для доступа в шаблоне

    # Чтобы использовать фильтр и список вместе, необходимо задать параметры
    def get_queryset(self):
        queryset = super().get_queryset()  # Получаем исходный QuerySet
        self.filterset = self.filterset_class(self.request.GET, queryset)  # Применяем фильтры
        return self.filterset.qs  # Возвращаем отфильтрованный QuerySet

class ItemDetailView(DetailView):
    model = Item
    template_name = 'item_detail.html'

class ItemCreateView(CreateView):
    model = Item
    fields = ['name', 'description', 'price']  # Добавлено поле цены
    template_name = 'item_form.html'
    success_url = reverse_lazy('item_list')

class ItemUpdateView(UpdateView):
    model = Item
    fields = ['name', 'description', 'price']  # Добавлено поле цены
    template_name = 'item_form.html'
    success_url = reverse_lazy('item_list')


class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'item_confirm_delete.html'
    success_url = reverse_lazy('item_list')
