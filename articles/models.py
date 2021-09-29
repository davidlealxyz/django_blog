from django.db import models
from django.contrib.auth.models import User
from django.http import request
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    title= models.CharField(max_length=100)
    body= models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment= models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_date',]

    def approve(self):
            self.approved_comment = True
            self.save()

    def __str__(self):
        return	self.title
		 

	
        



class Comment(models.Model):
    post = models.ForeignKey('Article' , on_delete=models.CASCADE, related_name='comments')
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date',]

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text