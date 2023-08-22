
# Importing necessary libraries
from django.db import models

# Revenue Models
class RevenueModel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Transaction(models.Model):
    revenue_model = models.ForeignKey(RevenueModel, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.revenue_model.name} - {self.amount}"
