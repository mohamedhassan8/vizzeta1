from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

class blog(models.Model):
    user_name=models.CharField(blank=True,null=True,max_length=100)
    img=models.ImageField(blank=True,null=True)
    title=models.CharField(max_length=100,blank=True,null=True,verbose_name=_('title'))
    detiles=models.TextField(blank=True,null=True)
    timecreate=models.DateTimeField(auto_now_add=True,blank=True,null=True)


    def __str__(self):
        return self.title


# Create your models here.
