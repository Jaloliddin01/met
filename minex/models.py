from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class Expense(models.Model):
    CATEGORY = (
        ('Food', 'Food'),
        ('Travel', 'Travel'),
        ('Shopping', 'Shopping'),
        ('Transportation', 'Transportation'),
        ('Entertainment', 'Entertainment'),
        ('Education', 'Education'),
        ('Health', 'Health'),
        ('Other', 'Other'),
    )

    amount = models.FloatField()
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description