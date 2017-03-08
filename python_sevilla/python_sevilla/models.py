from django.db import models


class posts(models.Model):
    name = models.CharField(verbose_name='Name', null=False, max_length=50)
    content = models.CharField(verbose_name='Content', null=False, max_length=300)
