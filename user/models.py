from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify
type=(('f','female'),('m','male'))
doctor_work=(('جلدية','جلدية'),('اسنان','اسنان'),('نفسي','نفسي'),('اطفال','اطفال حديثي الولادة'),('مخ','مخ واعصاب'),('عظام','عظام'),('نساء','نساء وتوليد'),('انف','انف واذن وحنجرة'),
             ('قلب','قلب واوعية دموية'),('امراض','امراض دم'),('اورام','اورام'),('باطنه','باطنه'),('تخسيس','تخسيس وتغذية'),('جاطفال','جراحة اطفال'),('جاورام','جراحة اورام'),('جاوعيه','جراحة اوعية دموية'),('جتجميل','جراحة تجميل'),('سمنه','جراحه سمنة ومناظير '))
class profiel(models.Model):
    Usr=models.OneToOneField(User,on_delete=models.CASCADE,verbose_name=('user'))
    who_i=models.CharField(max_length=100)
    age=models.IntegerField(blank=True,null=True)
    subtitle=models.CharField(max_length=100,null=True)
    timecreate=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    Specialist_doctor=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)
    address_detail=models.CharField(max_length=100,null=True)
    price=models.IntegerField(blank=True,null=True)
    Waiting_time=models.IntegerField(blank=True,null=True)
    working_hours=models.IntegerField(blank=True,null=True)
    numper=models.IntegerField(blank=True,null=True)
    img=models.ImageField(null=True)
    slug=models.SlugField(blank=True,null=True)
    nationl = models.CharField(max_length=100, null=True)
    facebook = models.CharField(max_length=100, null=True)
    google = models.CharField(max_length=100, null=True)
    twitter = models.CharField(max_length=100, null=True)
    doctor_type =models.CharField(choices=type,blank=True,null=True,max_length=100)
    doctor_jop=models.CharField(choices=doctor_work,blank=True,null=True,max_length=100)
    img1 = models.ImageField(null=True)
    img2=models.ImageField(null=True)
    img3=models.ImageField(null=True)
    img4 = models.ImageField(null=True)
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.Usr.username)
        super(profiel,self).save(*args,**kwargs)

    def __str__(self):
        return self.who_i
def seingnel(sender,**kwargs):
    if kwargs ['created']:
        profiel.objects.create(Usr=kwargs['instance'])
post_save.connect(seingnel,sender=User)


class pest_profiel(models.Model):
    pest_pro = models.OneToOneField(profiel, on_delete=models.CASCADE, verbose_name=('profiel'))
    who_i=models.CharField(max_length=100)
    img = models.ImageField(null=True)
    doctor_jop = models.CharField(choices=doctor_work, blank=True, null=True, max_length=100)
# Create your models here.

