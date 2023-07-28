from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Follow, User


class UserAdmin(BaseUserAdmin):
    list_display = (
        'username',
        'id',
        'email',
        'first_name',
        'last_name',
    )
    list_filter = ('email', 'first_name')
    search_fields = (
        'username',
        'email',
        'first_name',)


admin.site.register(Follow)
admin.site.register(User, UserAdmin)
