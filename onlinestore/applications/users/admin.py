from django.contrib import admin
#
from .models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'email',
        'full_name',
        'date_birth',
        'address',
        'phone',
        'marketingaccept',
        'cod_activated',
        'is_staff',
        'is_active',
        'otp_base32',
        'login_otp',
        'use_login_otp',
        'created_at' ,
    )

admin.site.register(User, UserAdmin)