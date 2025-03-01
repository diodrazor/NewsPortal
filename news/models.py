from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        self.rating = 0
        posts = Post.objects.filter(author = self)
        comments = Comment.objects.filter(user = self.user)
        posts_comments = Comment.objects.filter(post__author = self)
        for _ in posts:
            self.rating += _.rating * 3
        for _ in comments:
            self.rating += _.rating
        for _ in posts_comments:
            self.rating += _.rating
        self.save()

class Category(models.Model):
    name = models.CharField(max_length=255, unique = True)

class Post(models.Model):
    article = 'AR'
    new = 'NW'
    KIND = [(article, 'Статья'),(new, 'Новость')]

    author = models.ForeignKey(Author, on_delete = models.CASCADE)

    kind = models.CharField(max_length=2,
                                choices=KIND,
                                default=article) # статья или новость по умолчанию статья

    time_in = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    category = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.rating = self.rating + 1
        self.save()
    def dislike(self):
        self.rating = self.rating - 1
        self.save()

    def preview(self):
        return self.text[:123] + '...'

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time_in = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating = self.rating + 1
        self.save()
    def dislike(self):
        self.rating = self.rating - 1
        self.save()
