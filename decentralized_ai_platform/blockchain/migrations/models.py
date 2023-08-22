
from django.db import models

class Transaction(models.Model):
    sender = models.CharField(max_length=30)
    receiver = models.CharField(max_length=30)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} sent {self.amount} to {self.receiver}'

class Block(models.Model):
    transactions = models.ManyToManyField(Transaction)
    previous_hash = models.CharField(max_length=64)
    nonce = models.IntegerField()
    hash = models.CharField(max_length=64)

    def __str__(self):
        return self.hash
