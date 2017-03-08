from django.core.urlresolvers import reverse_lazy
from django.views import generic

from .models import posts
from .forms import CreatePostForm


class PostCreateView(generic.CreateView):
    model = posts
    form_class = CreatePostForm
    success_url = reverse_lazy('index')
    template_name = 'python_sevilla/create.html'
