# Generated by Django 4.0.6 on 2022-09-15 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoBlogApp', '0012_comment_is_liked_post_is_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='is_liked',
        ),
        migrations.RemoveField(
            model_name='post',
            name='is_liked',
        ),
    ]
