from django.contrib import admin
from .models import my_work
# Register your models here.

# class my_work(admin.ModelAdmin):
#     list_display = ('name', 'description',)

admin.site.register(my_work)

