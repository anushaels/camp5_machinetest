from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add_flight/', views.add_flight, name='add_flight'),
    path('edit_flight/<int:flight_id>/', views.edit_flight, name='edit_flight'),
    path('select_flight_to_edit/', views.select_flight_to_edit, name='select_flight_to_edit'),
    path('view_all_flights/', views.view_all_flights, name='view_all_flights'),
    path('delete_flight/<int:flight_id>/', views.delete_flight, name='delete_flight'),
    path('search_by_id/', views.search_by_id, name='search_by_id'),
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
