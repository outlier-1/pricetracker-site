from django.contrib import admin
from .models import Product,Category,PriceDetail,Track,Website
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(PriceDetail)
admin.site.register(Track)
admin.site.register(Website)

