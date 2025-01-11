from django.contrib import admin
from .models import (
    Category,
    ShopItem,
    SliderForItem
)


class SliderImageInline(admin.StackedInline):
    model = SliderForItem
    can_delete = False
    verbose_name_plural = 'Изображения для слайдера'
    extra = 1
    max_num = 3

class ItemAdmin(admin.ModelAdmin):
    inlines = [SliderImageInline]


admin.site.register(Category)
admin.site.register(ShopItem, ItemAdmin)
