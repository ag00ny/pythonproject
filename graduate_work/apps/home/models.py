from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class ShopItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Название категории')
    name = models.CharField(max_length=100, verbose_name='Название товара')
    gender = models.CharField(max_length=50, verbose_name="Мужское/женское", default='unisex',
                              help_text="указывать либо 'men', либо 'women', с маленькой буквы")
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    stock = models.IntegerField(default=0, verbose_name='Кол-во товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена товара')
    image = models.ImageField(upload_to='shop_items/%Y/%m/%d/', verbose_name="Изображение товара",
                              blank=True, null=True)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Скидка на товар',
                                         blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class SliderForItem(models.Model):
    item = models.ForeignKey(ShopItem, on_delete=models.CASCADE,
                             verbose_name='Товар', related_name='slider_for_item')
    photos = models.ImageField(upload_to='items_slides/%Y/%m/%d/', verbose_name="Изображения для слайдера")
    class Meta:
        verbose_name = 'Фото для слайдера'
        verbose_name_plural = 'Фото для слайдеров'


