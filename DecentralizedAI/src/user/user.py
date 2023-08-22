
import os
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    User model - Add any additional fields you need
    """
    is_online = models.BooleanField(default=False)
    last_seen = models.DateTimeField(null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return self.username

    def get_profile_picture(self):
        if self.profile_picture and hasattr(self.profile_picture, 'url'):
            return self.profile_picture.url
        else:
            return os.path.join('static', 'images', 'default_profile_picture.png')

    def is_user_online(self):
        return self.is_online

    def update_last_seen(self):
        self.last_seen = timezone.now()
        self.save()

    def update_online_status(self, status):
        self.is_online = status
        self.save()
