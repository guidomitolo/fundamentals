# no view functions, no use of render
# from django.shortcuts import render

from .models import Post

# built-in/default django OBJECTS for VIEWS
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# built-in/default django OBJECTS for "decorate" (control login/out USERS) VIEW OBJECTS
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['date_posted']

    # reference
    # home/post_list
    # <app>/<model>_<viewype>.html

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

    # reference
    # arena/post_detail
    # <app>/<model>_<viewype>.html


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # OVERRIDE form_valid built-in method
    # add author and then return form_valid method + author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # OVERRIDE form_valid built-in method
    # add author and then return form_valid method + author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/arena'

    # OVERRIDE test_func built-in method
    # check author
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False