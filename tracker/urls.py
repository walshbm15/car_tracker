from django.urls import path

from . import views

app_name = 'tracker'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:car_id>/', views.detail, name='detail'),
    path('<str:car_id>/service', views.add, name='add'),
]
