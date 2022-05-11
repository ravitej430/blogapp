
from django.db import models
from django.urls import reverse

class Book(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    author=models.ForeignKey('auth.user',on_delete=models.CASCADE) 
    #img=models.ImageField(blank=True)       
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", args=[str(self.id)])
    