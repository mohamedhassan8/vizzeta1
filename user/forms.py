from django import forms
from django.contrib.auth.models import User
from .models import profiel
from django.contrib.auth.forms import UserCreationForm
class createuser(UserCreationForm):
    username=forms.CharField()
    first_name=forms.CharField()
    last_name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','first_name','last_name','password')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = profiel
        fields = ['who_i', 'age', 'subtitle','Specialist_doctor', 'address','address_detail', 'price','Waiting_time', 'working_hours','numper', 'img', 'nationl','facebook', 'google', 'twitter','doctor_type', 'doctor_jop','img1','img2','img3','img4']
        '''
class prfieluser(UserCreationForm):

    class Meta:
        model = profiel
        fields = ('who_i','age')'''