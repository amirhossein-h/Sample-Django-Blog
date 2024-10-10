from django.db import models
from django.contrib.auth.models import User

class ContactMe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    email = models.EmailField(max_length=254)
    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}: {self.text[:10]}"
