from django.db import models
from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    image = models.URLField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    web= models.URLField(max_length=200, blank=True)
   
    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    need= models.TextField(blank=True)
    tags= models.ManyToManyField(Category, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    web= models.URLField(max_length=200, blank=True)
    github= models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.name

class Value(models.Model):
    name = models.CharField(max_length=100)
    color= models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Work(models.Model):
    name= models.CharField(max_length=100)
    description= models.TextField()
    tags= models.ManyToManyField(Value, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    web= models.URLField(max_length=200, blank=True)
    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    content= RichTextField(default='')
    # content_upload= RichTextUploadingField(default='')
    image = models.ImageField(upload_to='images/', blank=True)
    def __str__(self):
        return self.title
