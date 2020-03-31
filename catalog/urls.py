from django.urls import path
from . import  views
app_name = 'catalog'


urlpatterns =[
    path('', views.product_list, name='core_product_list'),
    path('<slug:slug>/', views.category, name='category'),
    path('produtos/<slug:slug>/', views.product, name='product'),



]

