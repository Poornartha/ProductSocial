from django.db import models
from django.contrib.auth.models import User


class Search(models.Model):
    search_term = models.CharField(max_length=100)
    users = models.ManyToManyField(User)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.search_term

