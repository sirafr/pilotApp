from django.urls import path 
from . import views

# domain.com/first_app/simple_view
# PILOT APP => MYSITE
# APP1 => First_app

urlpatterns = [
    path('',views.simple_view) #domain.com/app1


]