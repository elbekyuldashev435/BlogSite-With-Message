from django.contrib import admin
from .models import Categories, Brands, Discount, Products, Gender
# Register your models here.


admin.site.register(Categories)
admin.site.register(Brands)
admin.site.register(Discount)
admin.site.register(Products)
admin.site.register(Gender)