from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import post
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

class postlistview(ListView):
    model = post
    template_name = 'home.html'

class postdetailview(DetailView):
    model = post
    template_name = 'post_detail.html'


class blogcreateview(CreateView):
    model = post
    template_name = 'post_new.html'
    fields = ['title','author', 'body']

class blogupdateview(UpdateView):
    model = post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class blogdeleteview(DeleteView):
    model = post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')