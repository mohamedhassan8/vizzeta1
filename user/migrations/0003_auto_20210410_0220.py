# Generated by Django 2.2.7 on 2021-04-10 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profiel_usr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiel',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
