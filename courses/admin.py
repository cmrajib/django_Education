from django.contrib import admin

# Register your models here.
from courses.models import Course, Category,Course_Curricularm, Course_Review
from instructor.models import Instructor







class CourseAdmin(admin.ModelAdmin):  # instead of ModelAdmin

    # # instructor_names came from model.py
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name' ,'instructor_names','category', 'price']
    search_fields = ['name', 'category', 'instructor' ]
    list_filter = ['category']

    def get_instructor(self, obj):
        return obj.instructor.name
    get_instructor.short_description = 'Instructor'

class CategoryAdmin(admin.ModelAdmin):  # instead of ModelAdmin
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Course , CourseAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.register(Course_Curricularm)
admin.site.register(Course_Review)

# class UserAdmin(admin.ModelAdmin):
#     list_display = (..., 'get_author')
#
#     def get_author(self, obj):
#         return obj.book.author
#     get_author.short_description = 'Author'
#     get_author.admin_order_field = 'book__author'




