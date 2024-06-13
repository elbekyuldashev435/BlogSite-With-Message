from django.db import models

# Create your models here.


class Gender(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'gender'

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


class Brands(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING, null=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'brand'

    def __str__(self):
        return f"{self.category.name} {self.name}"


class Discount(models.Model):
    discount = models.IntegerField(default=0)

    class Meta:
        db_table = 'discount'

    def __str__(self):
        return f"{self.discount} %"


class Products(models.Model):
    brand = models.ForeignKey(Brands, on_delete=models.DO_NOTHING, null=True)
    image = models.ImageField(upload_to='product_img/', blank=True, null=True, default='default_img/product_img.png')
    info = models.TextField()
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    discount_price = models.ForeignKey(Discount, blank=True, null=True, on_delete=models.DO_NOTHING)
    gender = models.ForeignKey(Gender, blank=True, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return f"{self.brand.name} {self.name}"
