from django.shortcuts import render, redirect, get_object_or_404
from .forms import (
    UserRegistrationForm,
    UserLoginForm,
    CommentForm
)
from .models import (
    Profile,
    Basket,
    BasketItem,
    Comment,
    Favorite
)
from apps.home.models import ShopItem
from django.contrib.auth import authenticate, login, logout


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return redirect('login')
        else:
            print(form.errors)
    else:

        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'profiles/registration.html', context)


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')

    else:
        form = UserLoginForm()
    context = {'form': form}

    return render(request, 'profiles/login.html', context)


def profile_view(request):
    return render(request, 'profiles/profile.html')


def get_or_create_basket(user):
    basket, created = Basket.objects.get_or_create(user=user)
    return basket


def basket_view(request):
    if request.user.is_authenticated:
        basket = get_or_create_basket(request.user)
        basket_items = BasketItem.objects.filter(basket=basket)
        context = {'items': basket_items}
        return render(request, 'profiles/basket.html', context)
    else:
        return redirect('login')


def add_to_basket(request, item_id):
    if request.user.is_authenticated:
        basket = get_or_create_basket(request.user)
        item = get_object_or_404(ShopItem, pk=item_id)
        basket_item, created = BasketItem.objects.get_or_create(basket=basket, item=item)
        if not created:
            basket_item.quantity += 1
        basket_item.save()
        return redirect('basket')
    else:
        return redirect('login')


def remove_from_basket(request, item_id):
    if request.user.is_authenticated:
        basket = get_or_create_basket(request.user)
        basket_item = get_object_or_404(BasketItem, basket=basket, id=item_id)
        basket_item.delete()
        return redirect('basket')
    else:
        return redirect('basket')


def logout_view(request):
    logout(request)
    return redirect('home')


def comments_view(request, item_id):
    item = get_object_or_404(ShopItem, id=item_id)
    comments = Comment.objects.filter(item=item).order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.item = item
            new_comment.save()
            return redirect('comments', item_id=item.id)
    else:
        form = CommentForm()

    context = {
        'item': item,
        'comments': comments,
        'form': form,
    }
    return render(request, 'profiles/comments.html', context)


def add_to_favorite(request, item_id):
    if request.user.is_authenticated:
        item = get_object_or_404(ShopItem, id=item_id)
        Favorite.objects.get_or_create(user=request.user, item=item)
        return redirect('favorite')
    else:
        return redirect('login')


def remove_from_favorite(request, item_id):
    if request.user.is_authenticated:
        item = get_object_or_404(ShopItem, id=item_id)
        Favorite.objects.filter(user=request.user, item=item).delete()
        return redirect('favorite')
    else:
        return redirect('login')


def favorites_view(request):
    if request.user.is_authenticated:

        favorites = Favorite.objects.filter(user=request.user).select_related('item')
        context = {'favorites': favorites}
        return render(request, 'profiles/favourites.html', context)
    else:
        return redirect('login')
