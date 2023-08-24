from django.urls import path, include
from myapp import views

urlpatterns=[
    path('', views.login_view, name='login'),
    path('index', views.index_view, name='index'),
    path('register', views.register_view, name='register'),
    path('registerdetails', views.patient_details_view, name='registerdetails'),
    path('consult/', views.consult_view, name='consult'),
    path('displaydetails/<int:user_id>/', views.user_details, name='displaydetails'),
    path('save_observation', views.save_observation, name='save_observation'),
]
