from django.contrib import admin

# Register your models here.
from django.utils.html import format_html

from instructor.models import Instructor, Skill, Department

class DepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class InstructorAdmin(admin.ModelAdmin):  # instead of ModelAdmin
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;"/>'.format(object.image.url))

    thumbnail.short_description = 'Photo'
    list_display = ['thumbnail', 'name' ,'department', 'Language']
    search_fields = ['name', 'department' ]
    list_filter = ['department']



admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Skill)
admin.site.register(Department, DepartmentAdmin)
