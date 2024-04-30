from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.IntegerField(default=0)  # New field for book inventory

    class Meta:
        indexes = [
            models.Index(fields=['price'], name='BookListAPI_price_idx')
        ]
