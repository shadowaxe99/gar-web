
from django.db import models

class INLP(models.Model):
    text = models.TextField()
    processed_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[:50]

    def save(self, *args, **kwargs):
        # Here we can add our iNLP processing logic
        self.processed_text = self.text  # Placeholder
        super().save(*args, **kwargs)
