# Generated by Django 3.1.5 on 2021-01-14 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishitem',
            name='description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
