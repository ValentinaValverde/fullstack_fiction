# Generated by Django 4.2.6 on 2023-10-18 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.TextField(null=True),
        ),
    ]