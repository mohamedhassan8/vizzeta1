from django.urls import path
from .views import passb1,profel,log,backlog,my_profile,crea,backcreate,profile,logout1,search
urlpatterns = [

    path('h/', passb1, name='pass1'),
    path('search/', search, name='search'),
    path('log/',log,name='log'),
    path('backlog/',backlog,name='backlog'),
    path('my/',my_profile,name='myi'),
    path('created/',crea,name='crea'),
    path('backcreate/',backcreate,name='backcreate'),
    path('profile/',profile,name='profile'),
    path('',logout1,name='logout'),
    path('<slug:slug>/', profel, name='profel'),
]
