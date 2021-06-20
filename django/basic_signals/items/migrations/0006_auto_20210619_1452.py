# Generated by Django 2.2 on 2021-06-19 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_auto_20210618_2121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='quantity_delivered',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity_ordered',
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(null=True, verbose_name='Amount'),
        ),
    ]