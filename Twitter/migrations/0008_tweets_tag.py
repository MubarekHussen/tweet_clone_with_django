# Generated by Django 3.2.18 on 2023-04-26 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Twitter', '0007_tweets_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweets',
            name='tag',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
