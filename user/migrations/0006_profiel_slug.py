# Generated by Django 2.2.7 on 2021-04-12 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_profiel_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiel',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
