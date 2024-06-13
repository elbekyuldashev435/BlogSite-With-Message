from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='users_image/', blank=True, null=True, default='default_img/default_user.png')

    class Meta:
        db_table = 'custom_user'

    def __str__(self):
        return f"User: {self.username}"