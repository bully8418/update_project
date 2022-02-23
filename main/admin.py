from django.contrib import admin

from .models import *

admin.site.register(Task)
admin.site.register(Category)
admin.site.register(Device)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
