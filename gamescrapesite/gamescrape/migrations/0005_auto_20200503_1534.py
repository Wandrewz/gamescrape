# Generated by Django 3.0.5 on 2020-05-03 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamescrape', '0004_game_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='amazonid',
        ),
        migrations.RemoveField(
            model_name='game',
            name='targetid',
        ),
        migrations.RemoveField(
            model_name='game',
            name='targetprice',
        ),
        migrations.RemoveField(
            model_name='game',
            name='targeturl',
        ),
        migrations.RemoveField(
            model_name='game',
            name='walmartid',
        ),
    ]
