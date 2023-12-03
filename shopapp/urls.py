from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('shop/products/', views.products, name='products'),
    path('shop/product/<int:id_product>', views.product, name='product'),
    path('shop/order/<int:id_order>', views.order, name='order'),
    path('shop/clients/', views.clients, name='clients'),
    path('shop/orders/', views.orders, name='orders'),
    path('shop/client_orders/<int:id_client>', views.client_orders, name='client_orders'),
    path('shop/client_products_sorted/<int:id_client>/<int:days>/', views.client_products_sorted, name='client_products_sorted'),
    path('shop/product_form/<int:id_product>', views.product_form, name='product_form'),
    path('shop/choice_product_id_form/', views.choice_product_by_id, name='choice_product_id_form'),
    path('shop/choice_products_by_client_by_days/', views.choice_products_by_client_by_days, name='choice_products_by_client_by_days'),
    path('shop/choice_product/', views.choice_product, name='choice_product'),
]