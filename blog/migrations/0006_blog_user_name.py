# Generated by Django 2.2.7 on 2021-04-23 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_blog_blo'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='user_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
