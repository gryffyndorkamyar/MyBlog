from django.shortcuts import render
from blog.models import Webcategory, Projectname, YourIdea, Contact, Skill, BlogPost

def index(request):
    webcategories = Webcategory.objects.all()
    projects = Projectname.objects.all().order_by('-created_at')[:6]  # نمایش 6 پروژه آخر
    ideas = YourIdea.objects.all()
    skills = Skill.objects.all().order_by('type', 'name')
    contacts = Contact.objects.all()
    blog_posts = BlogPost.objects.filter(is_published=True).order_by('-published_at')[:3]  # نمایش 3 پست آخر
    
    context = {
        'webcategories': webcategories,
        'projects': projects,
        'ideas': ideas,
        'skills': skills,
        'contacts': contacts,
        'blog_posts': blog_posts,
    }
    
    return render(request, 'index.html', context)


