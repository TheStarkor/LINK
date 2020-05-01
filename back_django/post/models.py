from django.db import models

class Post(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  title = models.CharField(max_length=200, blank=False)
  author = models.CharField(max_length=20, blank=True, default='')
  pw = models.CharField(max_length=12, blank=True, default='')
  content = models.TextField()


  class Meta:
    ordering = ('created',)


  def __str__(self):
    return self.title