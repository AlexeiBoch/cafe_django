from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.decorators.http import require_POST

from shop.models import Category, Product
from shop.cart import Cart
from shop.forms import CartAddProductForm


class ProductListView(View):
    def get(self, request):
        categories = Category.objects.all()
        cart_product_form = CartAddProductForm()
        return render(request, 'shop/main.html', context={'categories':categories,
                                                          'cart_product_form':cart_product_form})
    
# cart

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('/')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'shop/cart.html', {'cart': cart})

def about_view(request):
    return render(request, 'shop/about.html')

def pay_view(request):
    cart = Cart(request)
    print(cart.get_total_price())
    if cart.get_total_price() == 0:
        return redirect('/') 
    return render(request, 'shop/pay.html', {'cart':cart})

def pay_done_view(request):
    cart = Cart(request)
    cart.clear()
    return render(request, 'shop/pay_done.html')

