# Generated by Django 3.0.8 on 2020-07-17 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0002_bookmark_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmark',
            old_name='owner',
            new_name='owners',
        ),
    ]
