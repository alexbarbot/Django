from django.urls import path
from . import views 

urlpatterns = [
	path('', views.index, name='index'),
	path('machines/', views.machine_list_view, name='machines'),
	path('machines_detail/<pk>', views.machine_detail_view, name='machine-detail'),
	path('add-machines/', views.machine_add_form, name='add-machines'),
	path('personnels/', views.personnel_list_view, name='personnels'),
	path('personnel/<pk>', views.machine_detail_view, name='personnel-detail'),
	path('add-personnel/', views.personnel_add_form, name='add-personnels'),

]

