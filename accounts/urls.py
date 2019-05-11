from django.conf.urls import url

from . import views


app_name = 'accounts'
urlpatterns = [
    url('registro/', views.register, name='register')
]
