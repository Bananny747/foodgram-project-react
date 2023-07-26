from django.contrib import admin

from .models import Follow, User


class UserAdmin(admin.ModelAdmin):
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
