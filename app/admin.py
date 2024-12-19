# admin.py
from django.contrib import admin
from .models import BlogPost, Feedback, Comment, Product, CartItem, Order

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'content')
    list_filter = ('published_date',)

    def has_add_permission(self, request):
        return request.user.is_superuser or request.user.username == 'admin'

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    search_fields = ('name',)
    list_filter = ('price', 'stock')

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Feedback)
admin.site.register(Comment)
admin.site.register(Product, ProductAdmin)
admin.site.register(CartItem)
admin.site.register(Order)