from django.urls import path
from .views import test,createpostFor
urlpatterns = [

    path('test/<int:slu>/', test,name='pass'),
    path('c/', createpostFor,name='createpostForm'),

]