from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Item

# ListView для отображения списка объектов
class ItemListView(ListView):
    model = Item
    template_name = 'item_list.html'

# DetailView для отображения деталей объекта
class ItemDetailView(DetailView):
    model = Item
    template_name = 'item_detail.html'

# CreateView для создания нового объекта
class ItemCreateView(CreateView):
    model = Item
    fields = ['name', 'description']
    template_name = 'item_form.html'
    success_url = reverse_lazy('item_list')

# UpdateView для обновления объекта
class ItemUpdateView(UpdateView):
    model = Item
    fields = ['name', 'description']
    template_name = 'item_form.html'
    success_url = reverse_lazy('item_list')

# DeleteView для удаления объекта
class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'item_confirm_delete.html'
    success_url = reverse_lazy('item_list')
