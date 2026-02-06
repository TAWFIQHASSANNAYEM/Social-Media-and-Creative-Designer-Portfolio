from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = "dashboard"

urlpatterns = [
    path("login/", views.DashboardLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("", views.DashboardHomeView.as_view(), name="home"),
    path("profile/", views.profile_edit, name="profile"),
    path("about/", views.AboutCardListView.as_view(), name="about_list"),
    path("about/new/", views.AboutCardCreateView.as_view(), name="about_create"),
    path("about/<int:pk>/edit/", views.AboutCardUpdateView.as_view(), name="about_edit"),
    path("about/<int:pk>/delete/", views.AboutCardDeleteView.as_view(), name="about_delete"),
    path("services/", views.ServiceListView.as_view(), name="service_list"),
    path("services/new/", views.ServiceCreateView.as_view(), name="service_create"),
    path("services/<int:pk>/edit/", views.ServiceUpdateView.as_view(), name="service_edit"),
    path("services/<int:pk>/delete/", views.ServiceDeleteView.as_view(), name="service_delete"),
    path("highlights/", views.HighlightListView.as_view(), name="highlight_list"),
    path("highlights/new/", views.HighlightCreateView.as_view(), name="highlight_create"),
    path("highlights/<int:pk>/edit/", views.HighlightUpdateView.as_view(), name="highlight_edit"),
    path("highlights/<int:pk>/delete/", views.HighlightDeleteView.as_view(), name="highlight_delete"),
    path("socials/", views.SocialLinkListView.as_view(), name="social_list"),
    path("socials/new/", views.SocialLinkCreateView.as_view(), name="social_create"),
    path("socials/<int:pk>/edit/", views.SocialLinkUpdateView.as_view(), name="social_edit"),
    path("socials/<int:pk>/delete/", views.SocialLinkDeleteView.as_view(), name="social_delete"),
    path("features/", views.FeatureListView.as_view(), name="feature_list"),
    path("features/new/", views.FeatureCreateView.as_view(), name="feature_create"),
    path("features/<int:pk>/edit/", views.FeatureUpdateView.as_view(), name="feature_edit"),
    path("features/<int:pk>/delete/", views.FeatureDeleteView.as_view(), name="feature_delete"),
    path("skills/", views.SkillListView.as_view(), name="skill_list"),
    path("skills/new/", views.SkillCreateView.as_view(), name="skill_create"),
    path("skills/<int:pk>/edit/", views.SkillUpdateView.as_view(), name="skill_edit"),
    path("skills/<int:pk>/delete/", views.SkillDeleteView.as_view(), name="skill_delete"),
    path("projects/", views.ProjectListView.as_view(), name="project_list"),
    path("projects/new/", views.ProjectCreateView.as_view(), name="project_create"),
    path("projects/<int:pk>/edit/", views.ProjectUpdateView.as_view(), name="project_edit"),
    path("projects/<int:pk>/delete/", views.ProjectDeleteView.as_view(), name="project_delete"),
    path("experience/", views.ExperienceListView.as_view(), name="experience_list"),
    path("experience/new/", views.ExperienceCreateView.as_view(), name="experience_create"),
    path("experience/<int:pk>/edit/", views.ExperienceUpdateView.as_view(), name="experience_edit"),
    path("experience/<int:pk>/delete/", views.ExperienceDeleteView.as_view(), name="experience_delete"),
]
