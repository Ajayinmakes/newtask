from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('loginn', views.loginn, name='login'),
    path('new page', views.newpage, name='new page'),
    path('registrationform', views.registrationform, name='registrationform'),
    path('thrissur', views.thrissur, name='thrissur'),
    path('kollam', views.kollam, name='kollam'),
    path('Eranamkulam', views.Eranamkulam, name='Eranamkulam'),
    path('palakkad', views.palakkad, name='palakad'),
    path('wayanad',views.wayanad, name='wayanad')

 ]
