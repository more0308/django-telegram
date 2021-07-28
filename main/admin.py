from django.contrib import admin
from .models import *

class AdminCurrency(admin.ModelAdmin):
    list_display = ['title', 'slug']
    list_display_links = ['title', 'slug']
    search_fields = ['title']
    prepopulated_fields = {"slug": ("title",)}

class AdminClient(admin.ModelAdmin):
    list_display = ['user_id', 'username', 'name', 'created_at']
    list_display_links = ['user_id', 'username']
    search_fields = ['username']
    ordering = ['created_at']

admin.site.register(Client, AdminClient)
admin.site.register(Currency, AdminCurrency)
