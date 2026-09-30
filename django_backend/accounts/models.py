from django.db import models
from django.contrib.auth.models import User


class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_holder_name = models.CharField(max_length=100)
    masked_card_number = models.CharField(max_length=19)
    last_four_digits = models.CharField(max_length=4)
    expiry_month = models.PositiveSmallIntegerField()
    expiry_year = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.card_holder_name} - {self.masked_card_number}"