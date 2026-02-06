from rest_framework import viewsets

from .models import (
    AboutCard,
    Category,
    Experience,
    Feature,
    Highlight,
    Project,
    Service,
    SiteProfile,
    Skill,
    SocialLink,
)
from .serializers import (
    AboutCardSerializer,
    CategorySerializer,
    ExperienceSerializer,
    FeatureSerializer,
    HighlightSerializer,
    ProjectSerializer,
    ServiceSerializer,
    SiteProfileSerializer,
    SkillSerializer,
    SocialLinkSerializer,
)

# API ViewSets
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-id')
    serializer_class = ProjectSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all().order_by('name')
    serializer_class = SkillSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all().order_by('-start_date')
    serializer_class = ExperienceSerializer


class SiteProfileViewSet(viewsets.ModelViewSet):
    queryset = SiteProfile.objects.all().order_by("-updated_at")
    serializer_class = SiteProfileSerializer


class AboutCardViewSet(viewsets.ModelViewSet):
    queryset = AboutCard.objects.all().order_by("order", "id")
    serializer_class = AboutCardSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().order_by("order", "id")
    serializer_class = ServiceSerializer


class HighlightViewSet(viewsets.ModelViewSet):
    queryset = Highlight.objects.all().order_by("order", "id")
    serializer_class = HighlightSerializer


class SocialLinkViewSet(viewsets.ModelViewSet):
    queryset = SocialLink.objects.all().order_by("order", "id")
    serializer_class = SocialLinkSerializer


class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all().order_by("order", "id")
    serializer_class = FeatureSerializer

