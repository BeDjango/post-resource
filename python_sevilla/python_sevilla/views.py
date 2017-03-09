from django.core.urlresolvers import reverse_lazy
from django.views import generic

from .models import posts
from .forms import CreatePostForm


class PostsView(generic.ListView):
    template_name = 'python_sevilla/list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return posts.objects.all()


class PostCreateView(generic.CreateView):
    model = posts
    form_class = CreatePostForm
    success_url = reverse_lazy('posts_lists')
    template_name = 'python_sevilla/create.html'


class PostDetailView(generic.DetailView):
    model = posts
    template_name = 'python_sevilla/detail.html'
    context_object_name = 'post'


class PostDeleteView(generic.DeleteView):
    model = posts
    success_url = reverse_lazy('posts_lists')
