# Generated by Django 4.0.6 on 2022-09-11 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoBlogApp', '0007_post_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='img',
            new_name='image',
        ),
    ]
