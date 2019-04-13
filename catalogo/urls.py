from django.urls import path

from . import views


app_name = 'catalogo'
urlpatterns = [
    path('', views.servicos, name='servicos'),
    path('<slug:slug>/', views.categoria, name='categoria'),

]
