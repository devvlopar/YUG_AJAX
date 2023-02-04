
from django.urls import path
from . import views 

urlpatterns = [
   path('',views.index, name='index'),
   path('add_data/',views.add_data, name='add_data'),
   path('delete_row/<int:pk>',views.delete_row, name='delete_row'),


]