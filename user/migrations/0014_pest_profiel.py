# Generated by Django 2.2.7 on 2021-04-27 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_profiel_img4'),
    ]

    operations = [
        migrations.CreateModel(
            name='pest_profiel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('who_i', models.CharField(max_length=100)),
                ('img', models.ImageField(null=True, upload_to='')),
                ('doctor_jop', models.CharField(blank=True, choices=[('جلدية', 'جلدية'), ('اسنان', 'اسنان'), ('نفسي', 'نفسي'), ('اطفال', 'اطفال حديثي الولادة'), ('مخ', 'مخ واعصاب'), ('عظام', 'عظام'), ('نساء', 'نساء وتوليد'), ('انف', 'انف واذن وحنجرة'), ('قلب', 'قلب واوعية دموية'), ('امراض', 'امراض دم'), ('اورام', 'اورام'), ('باطنه', 'باطنه'), ('تخسيس', 'تخسيس وتغذية'), ('جاطفال', 'جراحة اطفال'), ('جاورام', 'جراحة اورام'), ('جاوعيه', 'جراحة اوعية دموية'), ('جتجميل', 'جراحة تجميل'), ('سمنه', 'جراحه سمنة ومناظير ')], max_length=100, null=True)),
                ('Usr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.profiel', verbose_name='profiel')),
            ],
        ),
    ]
