from django.db import models
from django.contrib.auth.models import User
from apps.home.models import ShopItem


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Basket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='basket')
    created_at = models.DateTimeField(auto_now_add=True)


class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey(ShopItem, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('basket', 'item')


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    item = models.ForeignKey(ShopItem, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('author', 'comment')


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    item = models.ForeignKey(ShopItem, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'item')
        verbose_name_plural = 'Favorites'


