from django.conf.urls import url

from . import views
from .feeds import LatestPostsFeed

urlpatterns = [
    url(r'^posts/$', views.PostsView.as_view(), name='posts_lists'),
    url(r'^posts/create/$', views.PostCreateView.as_view(), name='post_create'),
    url(r'^posts/(?P<pk>[-\w]+)/$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^posts/(?P<pk>[-\w]+)/delete/$', views.PostDeleteView.as_view(), name='post_delete'),
    url(r'^feeds/$', LatestPostsFeed(), name='feeds'),
]

