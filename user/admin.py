from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active', 'profile_image_preview')
    list_filter = ('role', 'is_staff', 'is_active')

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'profile_image', 'bio')}),
        ('Permissions', {'fields': ('role', 'is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'role', 'is_staff', 'is_active', 'profile_image', 'bio')}
        ),
    )

    search_fields = ('email', 'username')
    ordering = ('email',)

    def profile_image_preview(self, obj):
        if obj.profile_image:
            return f'<img src="{obj.profile_image.url}" width="50" height="50" style="border-radius:50%"/>'
        return "No Image"
    profile_image_preview.allow_tags = True
    profile_image_preview.short_description = "Profile Image"

admin.site.register(User, CustomUserAdmin)
