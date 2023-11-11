from django.urls import path
from . import views
urlpatterns = [
     path('',views.index,name='index'),
     path('new',views.create,name='create'),
     path('edit/<int:p>',views.edit,name='edit'),
     path('delete/<int:p>',views.delete_itm,name='delete'),
]
