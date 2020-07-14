# Generated by Django 3.0.8 on 2020-07-14 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='TITLE')),
                ('url', models.URLField(unique=True, verbose_name='URL')),
            ],
        ),
    ]
