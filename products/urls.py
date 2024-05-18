from django.urls import path
from .views import *


app_name = 'products'
urlpatterns = [
    path('book-list/', BookListView.as_view(), name='book-list'),
    path('detail/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('delete/<int:pk>', BookDeleteView.as_view(), name='book-delete'),
    path('create/', BookCreateView.as_view(), name='book-create'),
]
