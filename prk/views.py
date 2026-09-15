from django.shortcuts import render
from django.db.models import Avg, Count, Max, Min
from .models import Category, Product


def index(request):
    products_with_category = Product.objects.select_related('category')

    categories_with_products = Category.objects.prefetch_related('products')

    price_stats = Product.objects.aggregate(
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )

    categories_stats = Category.objects.annotate(
        product_count=Count('products'),
        avg_price=Avg('products__price')
    )

    context = {
        'products': products_with_category,
        'categories': categories_with_products,
        'price_stats': price_stats,
        'categories_stats': categories_stats,
    }
    return render(request, 'prk/index.html', context)