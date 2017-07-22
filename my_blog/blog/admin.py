from django.contrib import admin
from .models import Category, Tag, Blog
# Register your models here.

admin.site.register([Category, Tag, Blog])