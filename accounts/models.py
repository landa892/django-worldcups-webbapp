from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = RichTextField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
