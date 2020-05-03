# Generated by Django 3.0.5 on 2020-05-02 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamescrape', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='image',
            field=models.ImageField(default='zelda.jpg', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='lowesturl',
            field=models.URLField(default='amazon.com'),
            preserve_default=False,
        ),
    ]
