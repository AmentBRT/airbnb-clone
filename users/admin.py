from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . import models


@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    """Custom User Admin Model"""

    fieldsets = BaseUserAdmin.fieldsets + (
        (
            'Custom Profile',
            {
                'fields': (
                    'avatar',
                    'gender',
                    'bio',
                    'birthdate',
                    'language',
                    'currency',
                    'superhost',
                )
            },
        ),
    )
    list_display = [
        'username',
        'first_name',
        'last_name',
        'email',
        'is_active',
        'language',
        'currency',
        'superhost',
        'is_staff',
        'is_superuser',
    ]
    list_filter = BaseUserAdmin.list_filter + ('superhost',)
