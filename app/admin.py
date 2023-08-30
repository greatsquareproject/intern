from django.contrib import admin
from .models import seller, buyer, products


admin.site.register(seller)
admin.site.register(buyer)
admin.site.register(products)
