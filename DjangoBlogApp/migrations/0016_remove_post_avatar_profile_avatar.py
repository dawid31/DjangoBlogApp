# Generated by Django 4.0.6 on 2022-09-17 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoBlogApp', '0015_alter_comment_options_remove_profile_avatar_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='avatar',
        ),
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=''),
        ),
    ]
