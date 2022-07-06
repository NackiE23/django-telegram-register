from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

User = get_user_model()


@admin.register(User)
class UserInAdmin(UserAdmin):
    search_fields = ['email', 'is_admin', 'is_staff', 'is_active']
    list_display = ['email', 'is_admin', 'is_staff', 'is_active']
    list_filter = ['is_admin', 'is_staff', 'is_active']

    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        ('Telegram information', {
            'fields': ('user_id', 'username', 'name')
        }),
        ('Permissions', {
            'fields': ('is_admin', 'is_staff', 'is_active')
        }),
    )

    add_fieldsets = (
        (None, {
            'fields': ('email', 'password1', 'password2')}
         ),
    )

    ordering = ('email',)
    filter_horizontal = ()
    readonly_fields = ('is_admin', 'is_staff', 'is_active')
