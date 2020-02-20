from django.urls import path
##going into  the directory
from . import views 




urlpatterns = [
    path('',views.post_list, name='post_list'),
]