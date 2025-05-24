from django.db import models
from django.contrib.auth.models import User

class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

    def __str__(self):
        return self.user.username

class Ticket(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()
    is_available = models.BooleanField(default=True)
    image = models.ImageField()

    def __str__(self):
        return f"Название: {self.title}, цена: {self.price}, Дата: {self.date}"
