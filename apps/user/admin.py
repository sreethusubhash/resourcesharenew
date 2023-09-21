from django.contrib import admin
from apps.user.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
#admin.site.register(User)
class CustomUser(UserAdmin):
    #adjustments
    fieldsets = UserAdmin.fieldsets + (
            ('Extra Fields', {'fields': ('title','bio')}),
    )
admin.site.register(User,CustomUser)
