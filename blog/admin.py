from django.contrib import admin
from blog.models import Webcategory , Projectname , YourIdea , Contact , Skill, BlogPost

class WebcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'project')

class ProjectnameAdmin(admin.ModelAdmin):
    list_display = ('name', 'projdetail', 'category')

class YourIdeaAdmin(admin.ModelAdmin):
    list_display = ('name', 'detail', 'phone_number')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'is_read', 'is_replied')
    list_per_page = 10

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'image')
    list_per_page = 10

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'is_published', 'is_featured', 'views_count', 'published_at')
    list_filter = ('is_published', 'is_featured', 'category', 'author', 'created_at')
    search_fields = ('title', 'content', 'excerpt')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_published', 'is_featured')
    readonly_fields = ('views_count', 'created_at', 'updated_at')
    
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('title', 'slug', 'content', 'excerpt', 'author', 'category')
        }),
        ('تصاویر', {
            'fields': ('featured_image',),
            'classes': ('collapse',)
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'keywords'),
            'classes': ('collapse',)
        }),
        ('تنظیمات', {
            'fields': ('is_published', 'is_featured', 'published_at')
        }),
        ('آمار', {
            'fields': ('views_count', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

admin.site.register(Webcategory, WebcategoryAdmin)
admin.site.register(Projectname, ProjectnameAdmin)
admin.site.register(YourIdea, YourIdeaAdmin)    
admin.site.register(Contact, ContactAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
