from django.urls import path, include
from myapp import views

urlpatterns=[
    path('', views.home_view, name='home'),
    path('about', views.about_view, name='about'),
    path('form', views.form_view, name='form'),
    path('addstudentdetails', views.addstudentdetails_view, name='addstudentdetails '),
    path('viewstudentdetails', views.viewstudentdetails_view, name='viewstudentdetails'),
    path('<int:pk>/', views.getstudent_view, name='getsinglestudent'),
    path('delete/<int:pk>/', views.deletestudent_view, name='viewstudentdetails'),

] 