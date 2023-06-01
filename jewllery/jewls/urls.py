from django.urls import path
from jewls import views
app_name = 'jewls'

urlpatterns = [
    path('', views.allProductCategory, name='allProductCategory'),
    path('<slug:c_slug>/', views.allProductCategory, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.productDetails, name='productCateDetail'),

]
