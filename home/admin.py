from django.contrib import admin
from .models import *
from django.core.exceptions import ValidationError
admin.site.site_header = "JavTechDigital Admin"
admin.site.site_title = "JavTechDigital Admin Portal"
admin.site.index_title = "Welcome to JavTechDigital Admin Portal"
# Register your models here.


class Disable_Admin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

    list_display = ['id', 'experience', 'cilents',
                    'projects', 'working', 'days', 'ratting', ]


admin.site.register(CompanyGrowth, Disable_Admin)


class ContactAdmin(admin.ModelAdmin):
    def has_add_permission(self, request) -> bool:
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False

    def has_delete_permission(self, request, obj=None) -> bool:
        return False
    readonly_fields = ['email', 'message']
    list_display = ['email', 'is_new', 'is_contacted']
    list_filter = ['is_new', 'is_contacted']


admin.site.register(Contact, ContactAdmin)


class OurTeamAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'post',
    ]
    search_fields = ['name']


admin.site.register(OurTeam, OurTeamAdmin)


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['customer', 'home_display']
    search_fields = ['home_display']


admin.site.register(Testimonial, TestimonialAdmin)


admin.site.register(Product)
