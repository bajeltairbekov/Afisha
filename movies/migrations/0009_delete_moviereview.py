# Generated by Django 5.1.4 on 2025-01-20 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_moviereview'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MovieReview',
        ),
    ]
