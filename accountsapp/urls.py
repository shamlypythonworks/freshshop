
from django.urls import path
from . import views
urlpatterns=[
    path('registerinfo/',views.registerinfo,name='registerinfo'),
    path('registerpage/',views.register,name='registerpage'),
    path('loginpage/',views.login,name='loginpage'),
    path('validation/',views.validation,name='validation')
]