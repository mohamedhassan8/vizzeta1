from django import forms
from .models import blog

class createpostForm(forms.Form):
    title=forms.CharField()
    detiles=forms.CharField()
    img=forms.ImageField()

    '''
    class Meta:
        model = blog
        fields = ['title', 'detiles', 'img']'''