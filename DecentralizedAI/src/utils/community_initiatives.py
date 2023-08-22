
from django.db import models

class CommunityInitiative(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    participants = models.ManyToManyField('User', related_name='initiatives')

    def __str__(self):
        return self.title

    def get_participants(self):
        return ", ".join([str(p) for p in self.participants.all()])

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
