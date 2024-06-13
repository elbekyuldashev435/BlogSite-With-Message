from django.shortcuts import render
from django.views import View
from .models import Categories, Brands, Products
# Create your views here.


class CategoryListView(View):
    def get(self, request):
        categories = Categories.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'category_list.html', context)


class BrandListView(View):
    def get(self, request, pk):
        brands = Brands.objects.filter(category_id=pk)
        context = {
            'brands': brands
        }
        return render(request, 'brand_list.html', context=context)


class ProductListView(View):
    def get(self, request, pk):
        products = Products.objects.filter(brand_id=pk)
        context = {
            'products': []
        }
        for product in products:
            discounted_price = None
            if product.discount_price:
                discounted_price = product.price - (product.price * product.discount_price.discount / 100)

            context['products'].append({
                'pk': product.pk,
                'image': product.image,
                'info': product.name,
                'price': product.price,
                'discounted_price': discounted_price,
                'discount': product.discount_price.discount if product.discount_price else None,
            })
        return render(request, 'product_list.html', context=context)