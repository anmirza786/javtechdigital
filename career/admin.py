from django.contrib import admin

# Register your models here.
from .models import (CourseForm,InternshipForm)

admin.site.register(CourseForm)
admin.site.register(InternshipForm)