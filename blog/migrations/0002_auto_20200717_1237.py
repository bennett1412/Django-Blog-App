# Generated by Django 3.0.6 on 2020-07-17 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='blog_user',
        ),
    ]
