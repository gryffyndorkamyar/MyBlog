from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import routers
from blog.models import Webcategory , Projectname , YourIdea , Contact , Skill , BlogPost
from blog.Serializers import WebcategorySerializers , ProjectnameSerializers , YourIdeaSerializers , ContactSerializers , SkillSerializers , BlogPostSerializers


class WebcategoryViewSet(viewsets.ModelViewSet):
    queryset = Webcategory.objects.all()
    serializer_class = WebcategorySerializers
    permission_classes = [permissions.IsAuthenticated]

class ProjectnameViewSet(viewsets.ModelViewSet):
    queryset = Projectname.objects.all()
    serializer_class = ProjectnameSerializers
    permission_classes = [permissions.IsAuthenticated]

class YourIdeaViewSet(viewsets.ModelViewSet):
    queryset = YourIdea.objects.all()
    serializer_class = YourIdeaSerializers
    permission_classes = [permissions.IsAuthenticated]

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers
    permission_classes = [permissions.IsAuthenticated]

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializers
    permission_classes = [permissions.IsAuthenticated]

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializers
    permission_classes = [permissions.IsAuthenticated]



