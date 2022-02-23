import decimal
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    device = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        if self.name:
            name = self.name
        else:
            name = self.device
        return str(name)


class Task(models.Model):
    img_foto = models.ImageField('Фото', blank=True, upload_to='D:\Проекты\Food_city\media')
    title = models.CharField('Название товара', max_length=100)
    tex_description = models.TextField('Техническое описание', blank=True, max_length=1000)
    description = models.TextField('Описание товара', max_length=1000)
    price = models.DecimalField(max_digits=13, decimal_places=2)
    category = models.ForeignKey('Category',  on_delete=models.PROTECT, null=True, related_name='products', verbose_name='Категория')
    device = models.ForeignKey('Device', on_delete=models.PROTECT, null=True, verbose_name='Бренд')

    def get_absolute_url(self):
        return reverse('product',  kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.img_foto.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['id']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Категория')
    posters = models.ImageField('Обложка', blank=True, upload_to='D:\Проекты\Food_city\media')

    def get_absolute_url(self):
        return reverse('categories',  kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Device(models.Model):
    title = models.CharField(max_length=150, db_index=True,  verbose_name='Устройства')

    def get_absolute_url(self):
        return reverse('model',  kwargs={'device_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Устройство'
        verbose_name_plural = 'Устройства'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)



    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
