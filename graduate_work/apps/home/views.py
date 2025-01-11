from django.shortcuts import render
from .models import (
    Category,
    ShopItem,
    SliderForItem
)
from django.core.paginator import Paginator


def home_view(request):
    return render(request, 'home/index.html')


def about_view(request):
    return render(request, 'home/about.html')


def contact_view(request):
    return render(request, 'home/contact.html')


def shop_view(request):
    items = ShopItem.objects.all()
    categories = Category.objects.all()

    sort_query = request.GET.get('sort')
    search_query = request.GET.get('q')
    if search_query:
        items = items.filter(name__icontains=search_query)
    if sort_query:
        items = items.order_by(sort_query)
    if sort_query and search_query:
        items = items.filter(name__icontains=search_query).order_by(sort_query)

    paginator = Paginator(items, 5)
    shop_page_num = request.GET.get('page')
    page_items = paginator.get_page(shop_page_num)

    context = {
        'categories': categories,
        'items': items,
        'page_items': page_items
    }
    return render(request, 'home/shop.html', context)


def category_items_view(request, pk):
    categories = Category.objects.all()
    category = Category.objects.get(pk=pk)
    items = ShopItem.objects.filter(category=category)
    sort_query = request.GET.get('sort')
    search_query = request.GET.get('q')
    if search_query:
        items = items.filter(name__icontains=search_query)
    if sort_query:
        items = items.order_by(sort_query)
    if sort_query and search_query:
        items = items.filter(name__icontains=search_query).order_by(sort_query)

    paginator = Paginator(items, 5)
    shop_page_num = request.GET.get('page')
    page_items = paginator.get_page(shop_page_num)

    context = {
        'categories': categories,
        'category': category,
        'page_items': page_items
    }
    return render(request, 'home/shop.html', context)


def item_detail_view(request, item_id):
    item = ShopItem.objects.get(pk=item_id)
    slides = [
        {'url': '/media/shop_items/2025/01/08/images.jpg'},
        {'url': '/media/shop_items/2025/01/08/Untitled.jpg'}
    ]
    context = {
        'slides': slides,
        'item': item
    }
    return render(request, 'home/item_details.html', context)


def item_gender_view(request, gender):
    categories = Category.objects.all()
    items = ShopItem.objects.filter(gender=gender)
    sort_query = request.GET.get('sort')
    search_query = request.GET.get('q')
    if search_query:
        items = items.filter(name__icontains=search_query)
    if sort_query:
        items = items.order_by(sort_query)
    if sort_query and search_query:
        items = items.filter(name__icontains=search_query).order_by(sort_query)
    paginator = Paginator(items, 5)
    shop_page_num = request.GET.get('page')
    page_items = paginator.get_page(shop_page_num)

    context = {
        'page_items': page_items,
        'gender': gender,
        'categories': categories
    }
    return render(request, 'home/shop.html', context)
