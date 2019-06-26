# Generated by Django 2.2.1 on 2019-06-25 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceries', '0002_remove_grocery_items_expiry_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grocery_items',
            name='man_date',
        ),
        migrations.AddField(
            model_name='grocery_items',
            name='amount',
            field=models.CharField(default=100000, max_length=128),
        ),
    ]