from django.urls import path
from .views import (
    home_view,
    about_view,
    contact_view,
    shop_view,
    item_detail_view,
    item_gender_view,
    category_items_view
)

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('shop/', shop_view, name='shop'),
    path('item/<int:item_id>', item_detail_view, name='item'),
    path('shop/<str:gender>/', item_gender_view, name='items_by_gender'),
    path('category/<int:pk>/', category_items_view, name='category')


]