from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'skills', views.SkillViewSet)
router.register(r'experiences', views.ExperienceViewSet)
router.register(r'profile', views.SiteProfileViewSet)
router.register(r'about-cards', views.AboutCardViewSet)
router.register(r'services', views.ServiceViewSet)
router.register(r'highlights', views.HighlightViewSet)
router.register(r'socials', views.SocialLinkViewSet)
router.register(r'features', views.FeatureViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
