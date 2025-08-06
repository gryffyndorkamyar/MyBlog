from rest_framework import serializers
from blog.models import Webcategory , Projectname , YourIdea , Contact , Skill , BlogPost


class WebcategorySerializers(serializers.modelseralizer):
    class meta:
        model = Webcategory
        fields = ['name' , 'type' , 'project' , 'image']

class ProjectnameSerializers(serializers.modelseralizer):
    class meta:
        model = Projectname
        fields = ['name' , 'projdetail' , 'projshortdetail' , 'image' , 'category' , 'status' , 'start_date' , 'end_date' , 'created_at' , 'updated_at']


class YourIdeaSerializers(serializers.modelserializer):
    class meta:
        model = YourIdea
        fields = ['name' , 'detail' , 'phone_number']

class ContactSerializers(serializers.modelserializer):
    class meta:
        model = Contact
        fields = ['name' , 'email' , 'phone_regax' , 'phone_number' , 'subject' , 'message' , 'is_read' , 'is_replied']


class SkillSerializers(serializers.modelserializer):
    class meta:
        model = Skill
        fields = ['name' , 'type' , 'image']

class BlogPostSerializers(serializers.modelserializer):
    class meta:
        model = BlogPost
        fields = ['title' , 'slug' , 'content' , 'excerpt' , 'author' , 'category' , 'featured_image' , 'meta_title' , 'meta_description' , 'keywords' , 'is_published' , 'is_featured' , 'views_count' , 'published_at' , 'created_at' , 'updated_at']




