from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Site(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='website_pics')
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    site_url = models.CharField(max_length=100, blank=True)
    developer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('site-detail', kwargs={'pk':self.pk })
