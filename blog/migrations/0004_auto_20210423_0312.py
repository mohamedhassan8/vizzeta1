# Generated by Django 2.2.7 on 2021-04-23 01:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210423_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
