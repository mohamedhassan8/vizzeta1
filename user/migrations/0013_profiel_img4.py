# Generated by Django 2.2.7 on 2021-04-25 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20210425_0601'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiel',
            name='img4',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
