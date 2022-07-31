from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.

class Tag(models.Model):
    captions = models.CharField(max_length=20)
    
    def __str__(self):
        return self.captions

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        return self.full_name()
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.TextField(max_length=100)
    image = models.ImageField(upload_to = "posts", null = True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null= True, related_name = "posts")
    tag = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=50)
    text = models.TextField(max_length= 400)
    post = models.ForeignKey(
        Post, on_delete = models.CASCADE, related_name = "comments")

