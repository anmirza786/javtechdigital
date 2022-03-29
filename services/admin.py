from turtle import title
from django.contrib import admin
from .models import (
    Category,
    Proposal,
    PortfolioProduct,
    PortfolioShowcase,
    Services, Category
)

# admin.site.register(PortfolioProduct)
# admin.site.register(PortfolioShowcase)
admin.site.register(Proposal)


class ServicesAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        title = obj.title
        slug = title
        obj.slug = slug.lower()
        obj.save()
        return super().save_model(request, obj, form, change)


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'category',

    ]


admin.site.register(Services, ServicesAdmin)
admin.site.register(Category, CategoryAdmin)
