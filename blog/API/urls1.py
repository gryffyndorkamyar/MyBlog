from django.urls import path , include
from .Webapp import WebcategoryViewSet , ProjectnameViewSet , YourIdeaViewSet , ContactViewSet , SkillViewSet , BlogPostViewSet
from rest_framework import DefaultRouter

router = DefaultRouter()
router.register(r'webcategory' , WebcategoryViewSet)
router.register(r'projectname' , ProjectnameViewSet)
router.register(r'youridea' , YourIdeaViewSet)
router.register(r'contact' , ContactViewSet)
router.register(r'skill' , SkillViewSet)
router.register(r'blogpost' , BlogPostViewSet)

path('api-blog/' , include(router.urls))


