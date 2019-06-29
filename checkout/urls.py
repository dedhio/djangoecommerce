from django.urls import path

from . import views


app_name = 'checkout'
urlpatterns = [
    path('carrinho/adicionar/<slug:slug>/', views.create_cart_item, name='create_cart_item'),

]