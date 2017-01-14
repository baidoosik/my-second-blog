from django.contrib import admin
from .models import Item,Category
# Register your models here

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', '가격']
    list_display_links = ['id','title']
    list_filter = ['created_date','category']
    search_fields = ['title']  # where ilike SQL 로서 수행

admin.site.register(Category)
