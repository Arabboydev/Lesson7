from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView,UpdateView,CreateView,DeleteView
from .models import Books
from django.contrib.auth.mixins import LoginRequiredMixin


class BookListView(ListView):
    model = Books
    template_name = 'book/book_list.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = Books
    template_name = 'book/book_detail.html'


class BookCreateView(CreateView):
    model = Books
    template_name = 'book/book_create.html'
    fields = '__all__'
    success_url = reverse_lazy('products:book-list')


class BookDeleteView(DeleteView):
    model = Books
    template_name = 'book/book_delete.html'
    success_url = reverse_lazy('products:book-list')






# class ListView(View):
#     def get(self, request):
#         book = Books.objects.all().order_by('-created_at')
#         return render(request, 'book/book_list.html', context={'book': book})


