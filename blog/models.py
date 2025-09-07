from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    category = models.ManyToManyField(Category)
    tags = TaggableManager()
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:single', args=[self.id])
