from django.contrib import admin
from .models import CustomUser


admin.site.register(CustomUser)




# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'username', 'first_name', 'last_name', 'is_staff', 'is_active','date_joined')
#     list_filter = ['is_staff', 'is_superuser', 'first_name', 'last_name']
#
#
# admin.site.register(CustomUser, CustomUserAdmin)
