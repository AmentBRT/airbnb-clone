from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
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
