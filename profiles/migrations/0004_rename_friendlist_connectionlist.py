# Generated by Django 4.0.3 on 2022-03-19 09:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0003_friendlist'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FriendList',
            new_name='ConnectionList',
        ),
    ]