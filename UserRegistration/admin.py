from django.contrib import admin


# Register your models here.
from django.utils.html import format_html

from UserRegistration.models import User


class UserAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;"/>'.format(object.image.url))

    thumbnail.short_description = 'Photo'
    list_display = ('email', 'thumbnail','full_name', 'address_1', 'phone','city')
    list_display_links = ('email', 'full_name')
    # list_filter = ('user__email','full_name','city')
    # list_editable = ('is_featured',)
    search_fields =('full_name', 'phone')
    list_per_page = 10




admin.site.register(User, UserAdmin)



