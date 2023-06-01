from . import views
from django.urls import path, include
app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>/',views.add_cart, name='add_cart'),
    path('', views.cart_details, name='cart_details'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('remove_all/<int:product_id>/', views.remove_all, name='remove_all')

]

