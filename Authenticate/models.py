from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
import uuid

class CustomUser(AbstractUser):
    """مدل User سفارشی برای پورتفولیو"""
    
    # فیلدهای اضافی
    bio = models.TextField(max_length=500, blank=True, verbose_name="بیوگرافی")
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name="تصویر پروفایل")
    
    # اطلاعات تماس
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="شماره تلفن باید در فرمت صحیح وارد شود."
    )
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True, verbose_name="تلفن")
    
    # اطلاعات حرفه‌ای
    job_title = models.CharField(max_length=100, blank=True, verbose_name="عنوان شغلی")
    company = models.CharField(max_length=100, blank=True, verbose_name="شرکت")
    location = models.CharField(max_length=100, blank=True, verbose_name="موقعیت جغرافیایی")
    
    # لینک‌های اجتماعی
    website = models.URLField(blank=True, verbose_name="وب‌سایت")
    github = models.URLField(blank=True, verbose_name="گیت‌هاب")
    linkedin = models.URLField(blank=True, verbose_name="لینکدین")
    twitter = models.URLField(blank=True, verbose_name="توییتر")
    instagram = models.URLField(blank=True, verbose_name="اینستاگرام")
    
    # تنظیمات
    is_public_profile = models.BooleanField(default=True, verbose_name="پروفایل عمومی")
    show_contact_info = models.BooleanField(default=True, verbose_name="نمایش اطلاعات تماس")
    
    # متا دیتا
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروزرسانی")

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"
        ordering = ['-date_joined']

    def __str__(self):
        return self.get_full_name() or self.username

    def get_absolute_url(self):
        return f"/profile/{self.username}/"

    @property
    def full_name(self):
        """نام کامل کاربر"""
        return self.get_full_name()

    @property
    def display_name(self):
        """نام نمایشی (نام کامل یا نام کاربری)"""
        return self.get_full_name() or self.username

    def get_social_links(self):
        """دریافت لینک‌های اجتماعی فعال"""
        links = {}
        if self.github:
            links['github'] = self.github
        if self.linkedin:
            links['linkedin'] = self.linkedin
        if self.twitter:
            links['twitter'] = self.twitter
        if self.instagram:
            links['instagram'] = self.instagram
        if self.website:
            links['website'] = self.website
        return links
