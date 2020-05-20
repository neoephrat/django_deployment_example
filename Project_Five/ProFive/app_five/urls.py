from django.conf.urls import url
from django.urls import path
from app_five import views


app_name="app_five"

urlpatterns = [
path('regestration/',views.regestration, name='regestration'),
path('login/', views.user_login, name='login')

]
