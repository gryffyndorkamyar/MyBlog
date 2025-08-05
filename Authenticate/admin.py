from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'job_title', 'company', 'is_active', 'date_joined']
    list_filter = ['is_active', 'is_staff', 'is_superuser', 'date_joined', 'groups']
    search_fields = ['username', 'first_name', 'last_name', 'email', 'job_title', 'company']
    ordering = ['-date_joined']
    
    # فیلدهای اضافی در لیست
    list_editable = ['is_active']
    
    # گروه‌بندی فیلدها در فرم ویرایش
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('اطلاعات شخصی', {
            'fields': ('first_name', 'last_name', 'email', 'bio', 'avatar')
        }),
        ('اطلاعات تماس', {
            'fields': ('phone', 'website'),
            'classes': ('collapse',)
        }),
        ('اطلاعات حرفه‌ای', {
            'fields': ('job_title', 'company', 'location'),
            'classes': ('collapse',)
        }),
        ('لینک‌های اجتماعی', {
            'fields': ('github', 'linkedin', 'twitter', 'instagram'),
            'classes': ('collapse',)
        }),
        ('تنظیمات', {
            'fields': ('is_public_profile', 'show_contact_info'),
            'classes': ('collapse',)
        }),
        ('دسترسی‌ها', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
            'classes': ('collapse',)
        }),
        ('تاریخ‌های مهم', {
            'fields': ('last_login', 'date_joined'),
            'classes': ('collapse',)
        }),
    )
    
    # فیلدهای اضافی در فرم ایجاد کاربر
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    
    # فیلدهای فقط خواندنی
    readonly_fields = ['last_login', 'date_joined', 'created_at', 'updated_at']
    
    def get_avatar_preview(self, obj):
        """نمایش پیش‌نمایش تصویر پروفایل"""
        if obj.avatar:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 50px; border-radius: 50%;" />',
                obj.avatar.url
            )
        return "بدون تصویر"
    get_avatar_preview.short_description = "تصویر پروفایل"
