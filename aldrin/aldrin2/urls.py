from . import views
from django.urls import path, include

urlpatterns = [

    path('demo1',views.demo1,name='demo1'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')

]
