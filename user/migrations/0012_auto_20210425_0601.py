# Generated by Django 2.2.7 on 2021-04-25 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_profiel_doctor_jop'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiel',
            name='img1',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='profiel',
            name='img2',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='profiel',
            name='img3',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]