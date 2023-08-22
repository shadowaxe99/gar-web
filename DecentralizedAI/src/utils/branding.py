
from django.db import models

class Branding(models.Model):
    logo = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=200)
    tagline = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_logo_url(self):
        if self.logo and hasattr(self.logo, 'url'):
            return self.logo.url
        else:
            return "/static/images/default_logo.png"

    def get_branding(self):
        return {
            "name": self.name,
            "tagline": self.tagline,
            "logo_url": self.get_logo_url()
        }
