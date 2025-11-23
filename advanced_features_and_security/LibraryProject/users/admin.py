from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Fieldsets define how fields are grouped and displayed
    fieldsets = UserAdmin.fieldsets + (
        # Only include date_of_birth
        ('Custom Fields', {'fields': ('date_of_birth',)}), 
    )
    # The 'add_fieldsets' is used on the "Add user" form
    add_fieldsets = UserAdmin.add_fieldsets + (
        # Only include date_of_birth
        ('Custom Fields', {'fields': ('date_of_birth',)}),
    )

# Register the CustomUser model with the custom admin class
admin.site.register(CustomUser, CustomUserAdmin)