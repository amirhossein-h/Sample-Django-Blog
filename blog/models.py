from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

class Index(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    cover = models.ImageField(upload_to="covers/")

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title


class Post(models.Model):
    index = models.ForeignKey(Index, on_delete=models.CASCADE, related_name="posts", null=True, blank=True)
    summary_text = models.TextField(blank=True, null=True)
    sub_title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="postimages/", null=True, blank=True)

    def __str__(self):
        return str(self.index)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Index, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}: {self.text[:10]}"

    def get_absolute_url(self):
        return reverse("post_detail_view", args=[self.post.id])


class General(models.Model):
    CHOICES = (
        ("casts", "casts"),
        ("seasons", "seasons"),
        ("about", "about"),
    )
    content_for = models.CharField(max_length=7 , choices= CHOICES)
    title = models.CharField(max_length=100, null=True, blank=True)
    summary_text = models.TextField(null=True, blank=True)
    sub_title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="others/", null=True, blank=True)

    def __str__(self):
        return f"{self.content_for}: {self.title}"


class TableData(models.Model):
    CHOICES = (
        ("casts", "casts"),
        ("seasons", "seasons"),
        ("about", "about"),
    )
    content_for = models.CharField(max_length=7 , choices= CHOICES)
    table_name = models.CharField(max_length=100, null=True, blank=True)
    related_to = models.CharField(max_length=100, null=True, blank=True)
    col_one = models.CharField(max_length=200, null=True, blank=True)
    col_two = models.CharField(max_length=200, null=True, blank=True)
    col_three = models.CharField(max_length=200, null=True, blank=True)
    col_four = models.CharField(max_length=200, null=True, blank=True)
    col_five = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.table_name} : {self.related_to}"
