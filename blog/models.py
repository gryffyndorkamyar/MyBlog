from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from Authenticate.models import CustomUser

class Webcategory(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    project = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.name
    

class Projectname(models.Model):
    STATUS_CHOICES = [
        ('completed', 'تکمیل شده'),
        ('in_progress', 'در حال انجام'),
        ('pending', 'در انتظار'),
    ]
    name = models.CharField(max_length=200)
    projdetail = models.CharField(max_length=2000)
    projshortdetail = models.CharField(max_length=200, default=True)
    image = models.ImageField(upload_to='images/' , null=True, blank=True)
    category = models.ForeignKey(Webcategory, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='completed', verbose_name="وضعیت")
    start_date = models.DateField(verbose_name="تاریخ شروع", null=True, blank=True)
    end_date = models.DateField(blank=True, null=True, verbose_name="تاریخ پایان")
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name="تاریخ بروزرسانی")


    class Meta:
        verbose_name = "پروژه"
        verbose_name_plural = "پروژه ها"
    
    def __str__(self):
        return self.name

class YourIdea(models.Model):
    name = models.CharField(max_length=200)
    detail = models.CharField(max_length=1000)
    phone_number = models.CharField(max_length=10)

    class Meta:
        verbose_name = "ایده"
        verbose_name_plural = "ایده ها"

    def __str__(self):
        return self.name

class Contact(models.Model):
    SUBJECT_CHOICES = [
        ('project', 'درخواست پروژه'),
        ('collaboration', 'همکاری'),
        ('consultation', 'مشاوره'),
        ('other', 'سایر'),
        ('idea', 'نظرات'),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="شماره تلفن باید به صورت +989XXXXXXXXX باشد"
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=15)
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES, default='other')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    is_replied = models.BooleanField(default=False)

    class Meta:
        verbose_name = "پیام"
        verbose_name_plural = "پیام ها"

    def __str__(self):
       return self.name    
    
class Skill(models.Model):
    SKILL_TYPE_CHOICES = [
        ('frontend', 'فرانت اند'),
        ('backend', 'بک اند'),
        ('fullstack', 'فول استک'),
        ('mobile', 'موبایل'),
        ('database', 'دیتابیس'),
        ('other', 'سایر'),
    ]
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=SKILL_TYPE_CHOICES, default='other')
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        verbose_name = "مهارت"
        verbose_name_plural = "مهارت ها"

    def __str__(self):
        return self.name
    

class BlogPost(models.Model):
    """مدل پست‌های بلاگ"""
    title = models.CharField(max_length=200, verbose_name="عنوان")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="اسلاگ")
    content = models.TextField(verbose_name="محتوا")
    excerpt = models.TextField(max_length=500, blank=True, verbose_name="خلاصه")
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="نویسنده")
    category = models.ForeignKey(Webcategory, on_delete=models.CASCADE, blank=True, null=True, verbose_name="دسته‌بندی")
    
    # تصاویر
    featured_image = models.ImageField(upload_to='blog/featured/', blank=True, verbose_name="تصویر ویژه")
    
    # SEO
    meta_title = models.CharField(max_length=60, blank=True, verbose_name="عنوان متا")
    meta_description = models.CharField(max_length=160, blank=True, verbose_name="توضیحات متا")
    keywords = models.CharField(max_length=200, blank=True, verbose_name="کلمات کلیدی")
    
    # وضعیت
    is_published = models.BooleanField(default=False, verbose_name="منتشر شده")
    is_featured = models.BooleanField(default=False, verbose_name="ویژه")
    views_count = models.PositiveIntegerField(default=0, verbose_name="تعداد بازدید")
    
    # تاریخ‌ها
    published_at = models.DateTimeField(blank=True, null=True, verbose_name="تاریخ انتشار")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروزرسانی")

    class Meta:
        verbose_name = "پست بلاگ"
        verbose_name_plural = "پست‌های بلاگ"
        ordering = ['-published_at', '-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.is_published and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)
    

