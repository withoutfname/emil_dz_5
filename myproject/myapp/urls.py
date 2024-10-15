from django.urls import path
from . import views

urlpatterns = [
    path('', views.ItemListView.as_view(), name='item_list'),
    path('<int:pk>/', views.ItemDetailView.as_view(), name='item_detail'),
    path('create/', views.ItemCreateView.as_view(), name='item_create'),
    path('<int:pk>/update/', views.ItemUpdateView.as_view(), name='item_update'),
    path('<int:pk>/delete/', views.ItemDeleteView.as_view(), name='item_delete'),
]
