from django.db import models



class User(models.Model):
    #id = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    admin = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    image = models.CharField(max_length=30)
    created_at = models.CharField(max_length=30)


class Blog(models.Model):
    #id = models.CharField(max_length=30)
    user_id = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    user_image = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    summary = models.CharField(max_length=30)
    content = models.CharField(max_length=30)
    created_at = models.CharField(max_length=30)


class Comment(models.Model):
    #id = models.CharField(max_length=30)
    blog_id = models.CharField(max_length=30)
    user_id = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    user_image = models.CharField(max_length=30)
    content = models.CharField(max_length=30)
    created_at = models.CharField(max_length=30)