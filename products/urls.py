from django.urls import path

import products
from .views import home, shop, search, shop_detail, update_book, delete_product, feedback, cart, add_to_cart

urlpatterns = [
    path('', home, name='home'),
    path('shop/', shop, name='shop'),
    path('search/', search, name='search'),
    path('<int:id>/shop_detail/', shop_detail, name='shop-detail'),
    path('<int:id>/update_detail/', update_book, name='update-detail'),
    path('<int:id>/delete_product/', delete_product, name='delete-product'),
    path('testimonial/', feedback, name='testimonial'),
    path('<int:id>/cart/', cart, name='cart'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
]