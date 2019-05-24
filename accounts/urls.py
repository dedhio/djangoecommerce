from django.urls import path

from . import views


app_name = 'accounts'
urlpatterns = [
    path('', views.minha_conta, name='minha_conta'),
    path('registro/', views.register, name='register'),
    path('atualizaUsuario/', views.atualiza_user, name='atualiza_user')
]
