from django.db import models


class UrlData(models.Model):
    url = models.CharField(max_length=200) 
    slug = models.CharField(max_length=17,unique=True)
    count = models.IntegerField(default=0)
    def __init___(url,slug):
        self.url = url
        self.slug = slug
        self.count = 0
    def __str__(self):
        return f"Short Url for: {self.url} is {self.slug}"
