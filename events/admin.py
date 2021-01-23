from django.contrib import admin

# Register your models here.
from django.utils.html import format_html

from events.models import EventModel, Category

class CategoryAdmin(admin.ModelAdmin):  # instead of ModelAdmin
    prepopulated_fields = {"slug": ("name",)}


class EventAdmin(admin.ModelAdmin):  # instead of ModelAdmin
    prepopulated_fields = {"slug": ("name",)}

    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;"/>'.format(object.image.url))

    list_display = ['name' ,'location','time_from', 'time_to', 'date']
    search_fields = ['name', 'location']
    list_filter = ['datetime']


admin.site.register(EventModel, EventAdmin)
admin.site.register(Category, CategoryAdmin)



