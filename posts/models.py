from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    url   = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(User)
    votes = models.IntegerField(default = 1)

    def date_fr(self):
        return self.pub_date.strftime('%b %d %Y')
