
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="homepage"),
    path('a',views.about,name="aboutpage"),
    path('b',views.contact,name="contactpage"),
    path('c',views.login,name="loginpage"),
]
