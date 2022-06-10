from django.urls import path 
from . import views

# domain.com/first_app/simple_view
# PILOT APP => MYSITE
# APP1 => First_app

urlpatterns = [
    path('<str:topic>/', views.news_view),
    path('<int:num1>/<int:num2>',views.add_view)
]