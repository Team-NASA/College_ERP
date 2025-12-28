from django.contrib import admin
from .models import Department
from .models import Subject

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display=('name', 'created_at')
    search_fields=('name',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display=('code', 'name', 'department')
    list_filter=('department',)
    search_fields=('code', 'name')
