# Generated by Django 5.1 on 2024-08-11 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='decription',
            new_name='description',
        ),
    ]
