from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Group, Post
from .forms import PostForm
from .constants import PAGE_COUNT


class PostListView(ListView):
    template_name = 'posts/index.html'
    context_object_name = 'posts'
    paginate_by = PAGE_COUNT

    def get_queryset(self):
        return Post.objects.all().select_related('author').select_related('group')


class GroupListView(ListView):
    template_name = 'posts/group_list.html'
    context_object_name = 'posts'
    paginate_by = PAGE_COUNT

    def get_queryset(self):
        return Post.objects.filter(
            group__slug=self.kwargs['slug']
        ).select_related('group').select_related('author')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['group'] = Group.objects.get(slug=self.kwargs['slug'])
        return context


class ProfileListView(ListView):
    template_name = 'posts/profile.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(
            author__username=self.kwargs['username']
        ).select_related('author').select_related('group')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = Post.objects.filter(author__username=self.kwargs['username'])
        context['posts_count'] = Post.objects.filter(author__username=self.kwargs['username']).count()
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    pk_url_kwarg = 'pk'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['text', 'group', 'author']
    template_name = 'posts/post_create.html'


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/post_create.html'
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_edit'] = True
        return context


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=self.kwargs['pk'])
        return context