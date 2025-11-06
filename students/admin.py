from django.contrib import admin
from .models import Student

admin.site.site_header = "Student Management System"
admin.site.site_title = "Student Management System Portal"
admin.site.index_title = "Welcome to the Student Management System"

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "course", "year_level")
    list_filter = ("course", "year_level")
    search_fields = ("name",)
    ordering = ("name",)
