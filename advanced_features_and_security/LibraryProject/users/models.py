from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _ 

class CustomUserManager(UserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not extra_fields.get('date_of_birth'):
            raise ValueError(_('The Date of Birth field must be set.'))
        return super().create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('date_of_birth', '1970-01-01') 
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return super().create_superuser(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    objects = CustomUserManager() 

    # Custom Field to Add
    date_of_birth = models.DateField(
        _('date of birth'), 
        null=True, 
        blank=True
    )

    # --- FIX: Set unique related_name for reverse lookups (E304 fix) ---
    # This prevents conflicts with the default User model's internal fields
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to.'),
        related_name='customuser_set', 
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='customuser_permissions_set', 
        related_query_name='customuser_permission',
    )
    # ----------------------------------------------------------------------

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'date_of_birth'] 

    def __str__(self):
        return self.usernamecode 