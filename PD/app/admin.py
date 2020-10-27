from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('username', 'email', 'is_staff','is_superuser', 'is_active',)
    list_filter = ('username', 'email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('User Info', {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'role')}
        ),
        ('Details', {
            'classes': ('wide',),
            'fields': ('lat', 'lon', 'organization')}
        ),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
        ),
        ('User Info', {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'role')}
        ),
        ('Details', {
            'classes': ('wide',),
            'fields': ('lat', 'lon', 'organization')}
        ),
        ('Permissions', {
                'fields': ('is_staff', 'is_active', 'is_superuser')
        })
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)



admin.site.register(Organization)
admin.site.register(Medicine)
admin.site.register(Note)
admin.site.register(Test)
admin.site.register(TestSession)
admin.site.register(Therapy)
admin.site.register(TherapyList)
admin.site.register(News)



class DataOneResource(ImportExportModelAdmin):
    
    class Meta:
        model = DataFileOne
        fields = '__all__'

class DataTwoResource(ImportExportModelAdmin):
    
    class Meta:
        model = DataFileTwo
        fields = '__all__'


admin.site.register(DataFileOne, DataOneResource)
admin.site.register(DataFileTwo, DataTwoResource)