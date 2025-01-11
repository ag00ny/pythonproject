from django.urls import path
from .views import (
    register_view,
    login_view,
    profile_view,
    basket_view,
    add_to_basket,
    remove_from_basket,
    logout_view,
    comments_view,
    add_to_favorite,
    remove_from_favorite,
    favorites_view
)
urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('basket/', basket_view, name='basket'),
    path('basket/add/<int:item_id>/', add_to_basket, name='add_to_basket'),
    path('logout/', logout_view, name='logout'),
    path('basket/remove/<int:item_id>/', remove_from_basket, name='remove_from_basket'),
    path('comments/item/<int:item_id>', comments_view, name='comments'),
    path('add_to_favorite/<int:item_id>', add_to_favorite, name='add_to_favorite'),
    path('remove_from_favorite/<int:item_id>', remove_from_favorite, name='remove_from_favorite'),
    path('favorite', favorites_view, name='favorite'),

]