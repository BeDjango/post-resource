from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import posts


class LatestPostsFeed(Feed):
    title = "Posts for bedjango starter"
    link = "/feeds/"
    description = "Updates on changes and additions to posts published in the starter."

    def items(self):
        return posts.objects.order_by('name')[:5]

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
