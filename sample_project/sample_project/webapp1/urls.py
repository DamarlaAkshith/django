from django.urls import path

from . import views
urlpatterns=[
   # path('',views.add_emp,name='add_emp'),
   # path('add_emp',views.add_emp,name='add_emp')
   path('', views.ApiOverview, name='home'),
   path('create/', views.add_emp, name='add_emp'),
   path('all/', views.view_emps, name='view_emps'),
   path('update/<int:pk>/', views.update_emp, name='update_emp'),
   path('employees/<int:pk>/delete/', views.delete_emp, name='delete_emp'),
]
