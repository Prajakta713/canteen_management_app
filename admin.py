from django.contrib import admin
from .models import Section, Item
from django.contrib import admin
from .models import Order, AdminNotification
# Register your models here.


admin.site.register(Section)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(AdminNotification)
