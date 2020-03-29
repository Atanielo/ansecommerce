from django.urls import path
from .views import index, contact, product, product_list



urlpatterns =[
    path('', index, name='core_index'),
    path('contato', contact, name='core_contact'),
    path('produto', product, name='core_product'),
    path('produto_lista', product_list, name='core_product_list'),
#    path('contato-novo', contato_novo, name='core_contato_novo'),

]

