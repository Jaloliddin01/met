# Generated by Django 4.2 on 2023-04-12 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(choices=[('Food', 'Food'), ('Travel', 'Travel'), ('Shopping', 'Shopping'), ('Transportation', 'Transportation'), ('Entertainment', 'Entertainment'), ('Education', 'Education'), ('Health', 'Health'), ('Other', 'Other')], max_length=20),
        ),
    ]