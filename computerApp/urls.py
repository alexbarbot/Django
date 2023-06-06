from django.urls import path
from . import views 

urlpatterns = [
	path('', views.index, name='index'),
	path('machines/', views.machine_list_view, name='machines'),
	path('machines_detail/<pk>', views.machine_detail_view, name='machine-detail'),
	path('add-machines/', views.machine_add_view, name='add-machines'),
	path('personnels/', views.personnel_list_view, name='personnels'),
	path('personnel_detail/<pk>', views.personnel_detail_view, name='personnel-detail'),
	path('add-personnels/', views.personnel_add_view, name='add-personnels'),
	path('delete-machines/', views.machine_delete_view, name='delete-machines'),
	path('delete-personnels/', views.personnel_delete_view, name='delete-personnels'),
	path('gestion/', views.gestion_view, name='gestion'),
]

