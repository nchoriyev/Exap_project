from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart
from .forms import ProductForm, UpdateProductForm, SearchForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def home(request):
    return render(request, 'index.html')


def shop(request):
    query = request.GET.get('search')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()

    context = {
        'products': products,
        'value': query  # To keep the search query in the search box
    }
    return render(request, 'shop.html', context)



def search(request):
    form = SearchForm(request.GET or None)
    products = Product.objects.all()
    if form.is_valid():
        keyword = form.cleaned_data.get('keyword')
        if keyword:
            products = products.filter(name__icontains=keyword)
    return render(request, 'search.html', {'form': form, 'products': products})


def shop_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'shop_detail.html', {'product': product})

@login_required()
def product_detail(request, id):
    product = Product.objects.get(id=id)
    if product:
        return render(request, 'shop_detail.html', {'product': product, 'message': "Successfully"})
    else:
        return render(request, 'shop_detail.html', {'message': "Not Found"})


def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('shop')


def create_booklist(request):
    if request.method == 'POST':
        formm = ProductForm(request.POST, request.FILES)
        if formm.is_valid():
            formm.save()
            return redirect('books')
        else:
            return render(request, 'create_product_to_list.html', {'formm': formm, "message": "Xatolik topildi"})
    formm = ProductForm()
    return render(request, 'create_product_to_list.html', {'formm': formm})


def update_book(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = UpdateProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('shop')
        else:
            return render(request, 'update_detail.html', {'form': form, "message": "Xatolik topildi"})
    form = UpdateProductForm
    return render(request, 'update_detail.html', {'form': form})

def feedback(request):
    return render(request, 'testimonial.html')


@login_required()
def cart(request):
        user = request.User
        products = Product.objects.filter(user=user)
        if User:
            if products:
                return render(request, 'cart.html', {'products': products, 'message': "Successfully"})
            else:
                return render(request, 'cart.html')

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Cart.objects.create(user=request.user, product=product)
    return redirect('cart')


