# Generated by Django 2.2.7 on 2021-04-12 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20210412_0442'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profiel',
            old_name='tytr',
            new_name='twitter',
        ),
    ]
