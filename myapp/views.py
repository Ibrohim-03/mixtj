from django.shortcuts import render,redirect
from .models import Product

def start(request):
    return render(request,'main.html')

def poisk(request):
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    products = Product.objects.all()
    if min_price:
        products = products.filter(price__gte = min_price)
    if max_price:
        products = products.filter(price__lte = max_price)

    search = request.GET.get('search')
    if search:
        products=products.filter(name__icontains = search)

    return render(request,'products.html',{'products':products})

def products(request):
    products = Product.objects.all()
    return render(request,'prod.html',{'products':products})

def details(request,id):
    product=Product.objects.get(id=id)
    return render(request,'detail.html',{'product':product})

def delete(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('spiska')

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        Product.objects.create(name=name,description=description,price=price,quantity=quantity)
        return redirect('spiska')


    return render(request,'create.html')

def update(request,id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
            n_name = request.POST.get('name')
            n_description = request.POST.get('description')
            n_price = request.POST.get('price')
            n_quantity = request.POST.get('quantity')

            product.name=n_name
            product.description=n_description
            product.price=n_price
            product.quantity=n_quantity
            product.save()
            return redirect('spiska')
    return render(request,'update.html')
