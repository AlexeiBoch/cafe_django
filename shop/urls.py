from django.urls import path, re_path
from shop.views import ProductListView, cart_add, cart_remove, cart_detail, about_view, pay_view, pay_done_view

urlpatterns = [
    path('', ProductListView.as_view(), name='main'),
    path('about/', about_view, name='about'),
    path('cart/', cart_detail, name='cart'),
    path('pay/', pay_view, name='pay'),
    path('pay-done/', pay_done_view, name='pay_done'),
    re_path('cart/add/(?P<product_id>\d+)/$', cart_add, name='cart_add'),
    re_path('cart/remove/(?P<product_id>\d+)/$', cart_remove, name='cart_remove'),
]