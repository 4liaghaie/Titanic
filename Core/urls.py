from django.urls import path
from crud import views

urlpatterns = [
    path('', views.passenger_list, name='passenger_list'),
    path('upload/', views.upload_file, name='upload_file'),
    path('create/', views.passenger_create_update, name='passenger_create'),  # For creating a new passenger
    path('update/<int:passenger_id>/', views.passenger_create_update, name='passenger_update'),  # For updating an existing passenger
    path('delete/<int:passenger_id>/', views.passenger_delete, name='passenger_delete'),
    path('delete_all/', views.delete_all_passengers, name='delete_all_passengers'),
    path('grid/', views.passenger_grid, name='passenger_grid'),
]