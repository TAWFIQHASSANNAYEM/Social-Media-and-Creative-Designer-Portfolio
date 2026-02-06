from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, TemplateView, UpdateView

from hitcount.models import HitCount
from portapp.models import (
    AboutCard,
    Experience,
    Feature,
    Highlight,
    Project,
    Service,
    SiteProfile,
    Skill,
    SocialLink,
)

from .forms import (
    AboutCardForm,
    ExperienceForm,
    FeatureForm,
    HighlightForm,
    ProjectForm,
    ServiceForm,
    SiteProfileForm,
    SkillForm,
    SocialLinkForm,
)


class DashboardHomeView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            total_hits = HitCount.objects.get(pk=1).hits
        except HitCount.DoesNotExist:
            total_hits = 0

        context["stats"] = [
            {"label": "Projects", "value": Project.objects.count()},
            {"label": "Skills", "value": Skill.objects.count()},
            {"label": "Experience", "value": Experience.objects.count()},
            {"label": "Services", "value": Service.objects.count()},
            {"label": "Highlights", "value": Highlight.objects.count()},
            {"label": "Features", "value": Feature.objects.count()},
            {"label": "Social Links", "value": SocialLink.objects.count()},
            {"label": "Site Visits", "value": total_hits},
        ]
        return context


class DashboardLoginView(LoginView):
    template_name = "dashboard/login.html"
    redirect_authenticated_user = True


class DashboardListView(LoginRequiredMixin, ListView):
    template_name = "dashboard/list.html"
    paginate_by = 20
    title = ""
    create_url_name = ""
    edit_url_name = ""
    delete_url_name = ""
    columns = []
    search_fields = []
    empty_message = "No items found."

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q", "").strip()
        if query and self.search_fields:
            q_filter = Q()
            for field in self.search_fields:
                q_filter |= Q(**{f"{field}__icontains": query})
            queryset = queryset.filter(q_filter)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "title": self.title,
                "create_url_name": self.create_url_name,
                "edit_url_name": self.edit_url_name,
                "delete_url_name": self.delete_url_name,
                "columns": self.columns,
                "search_query": self.request.GET.get("q", ""),
                "empty_message": self.empty_message,
            }
        )
        return context


class DashboardCreateView(LoginRequiredMixin, CreateView):
    template_name = "dashboard/form.html"
    title = ""
    cancel_url = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"title": self.title, "cancel_url": self.cancel_url})
        return context


class DashboardUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "dashboard/form.html"
    title = ""
    cancel_url = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"title": self.title, "cancel_url": self.cancel_url})
        return context


class DashboardDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "dashboard/confirm_delete.html"
    title = ""
    cancel_url = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"title": self.title, "cancel_url": self.cancel_url})
        return context


@login_required
def profile_edit(request):
    profile, _ = SiteProfile.objects.get_or_create(pk=1)
    if request.method == "POST":
        form = SiteProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("dashboard:profile")
    else:
        form = SiteProfileForm(instance=profile)
    return render(
        request,
        "dashboard/form.html",
        {"form": form, "title": "Edit Site Profile", "cancel_url": "dashboard:home"},
    )


class AboutCardListView(DashboardListView):
    model = AboutCard
    title = "About Cards"
    create_url_name = "dashboard:about_create"
    edit_url_name = "dashboard:about_edit"
    delete_url_name = "dashboard:about_delete"
    search_fields = ["title", "body"]
    columns = [
        {"name": "title", "label": "Title"},
        {"name": "order", "label": "Order"},
        {"name": "is_active", "label": "Active"},
    ]


class AboutCardCreateView(DashboardCreateView):
    model = AboutCard
    form_class = AboutCardForm
    title = "Add About Card"
    success_url = reverse_lazy("dashboard:about_list")
    cancel_url = "dashboard:about_list"


class AboutCardUpdateView(DashboardUpdateView):
    model = AboutCard
    form_class = AboutCardForm
    title = "Edit About Card"
    success_url = reverse_lazy("dashboard:about_list")
    cancel_url = "dashboard:about_list"


class AboutCardDeleteView(DashboardDeleteView):
    model = AboutCard
    title = "Delete About Card"
    success_url = reverse_lazy("dashboard:about_list")
    cancel_url = "dashboard:about_list"


class ServiceListView(DashboardListView):
    model = Service
    title = "Services"
    create_url_name = "dashboard:service_create"
    edit_url_name = "dashboard:service_edit"
    delete_url_name = "dashboard:service_delete"
    search_fields = ["title", "body"]
    columns = [
        {"name": "title", "label": "Title"},
        {"name": "order", "label": "Order"},
        {"name": "is_active", "label": "Active"},
    ]


class ServiceCreateView(DashboardCreateView):
    model = Service
    form_class = ServiceForm
    title = "Add Service"
    success_url = reverse_lazy("dashboard:service_list")
    cancel_url = "dashboard:service_list"


class ServiceUpdateView(DashboardUpdateView):
    model = Service
    form_class = ServiceForm
    title = "Edit Service"
    success_url = reverse_lazy("dashboard:service_list")
    cancel_url = "dashboard:service_list"


class ServiceDeleteView(DashboardDeleteView):
    model = Service
    title = "Delete Service"
    success_url = reverse_lazy("dashboard:service_list")
    cancel_url = "dashboard:service_list"


class HighlightListView(DashboardListView):
    model = Highlight
    title = "Highlights"
    create_url_name = "dashboard:highlight_create"
    edit_url_name = "dashboard:highlight_edit"
    delete_url_name = "dashboard:highlight_delete"
    search_fields = ["label", "value"]
    columns = [
        {"name": "value", "label": "Value"},
        {"name": "label", "label": "Label"},
        {"name": "order", "label": "Order"},
        {"name": "is_active", "label": "Active"},
    ]


class HighlightCreateView(DashboardCreateView):
    model = Highlight
    form_class = HighlightForm
    title = "Add Highlight"
    success_url = reverse_lazy("dashboard:highlight_list")
    cancel_url = "dashboard:highlight_list"


class HighlightUpdateView(DashboardUpdateView):
    model = Highlight
    form_class = HighlightForm
    title = "Edit Highlight"
    success_url = reverse_lazy("dashboard:highlight_list")
    cancel_url = "dashboard:highlight_list"


class HighlightDeleteView(DashboardDeleteView):
    model = Highlight
    title = "Delete Highlight"
    success_url = reverse_lazy("dashboard:highlight_list")
    cancel_url = "dashboard:highlight_list"


class SocialLinkListView(DashboardListView):
    model = SocialLink
    title = "Social Links"
    create_url_name = "dashboard:social_create"
    edit_url_name = "dashboard:social_edit"
    delete_url_name = "dashboard:social_delete"
    search_fields = ["label", "url", "icon"]
    columns = [
        {"name": "label", "label": "Label"},
        {"name": "url", "label": "URL"},
        {"name": "icon", "label": "Icon"},
        {"name": "order", "label": "Order"},
        {"name": "is_active", "label": "Active"},
    ]


class SocialLinkCreateView(DashboardCreateView):
    model = SocialLink
    form_class = SocialLinkForm
    title = "Add Social Link"
    success_url = reverse_lazy("dashboard:social_list")
    cancel_url = "dashboard:social_list"


class SocialLinkUpdateView(DashboardUpdateView):
    model = SocialLink
    form_class = SocialLinkForm
    title = "Edit Social Link"
    success_url = reverse_lazy("dashboard:social_list")
    cancel_url = "dashboard:social_list"


class SocialLinkDeleteView(DashboardDeleteView):
    model = SocialLink
    title = "Delete Social Link"
    success_url = reverse_lazy("dashboard:social_list")
    cancel_url = "dashboard:social_list"


class FeatureListView(DashboardListView):
    model = Feature
    title = "Features"
    create_url_name = "dashboard:feature_create"
    edit_url_name = "dashboard:feature_edit"
    delete_url_name = "dashboard:feature_delete"
    search_fields = ["title", "body"]
    columns = [
        {"name": "title", "label": "Title"},
        {"name": "order", "label": "Order"},
        {"name": "is_active", "label": "Active"},
    ]


class FeatureCreateView(DashboardCreateView):
    model = Feature
    form_class = FeatureForm
    title = "Add Feature"
    success_url = reverse_lazy("dashboard:feature_list")
    cancel_url = "dashboard:feature_list"


class FeatureUpdateView(DashboardUpdateView):
    model = Feature
    form_class = FeatureForm
    title = "Edit Feature"
    success_url = reverse_lazy("dashboard:feature_list")
    cancel_url = "dashboard:feature_list"


class FeatureDeleteView(DashboardDeleteView):
    model = Feature
    title = "Delete Feature"
    success_url = reverse_lazy("dashboard:feature_list")
    cancel_url = "dashboard:feature_list"




class SkillListView(DashboardListView):
    model = Skill
    title = "Skills"
    create_url_name = "dashboard:skill_create"
    edit_url_name = "dashboard:skill_edit"
    delete_url_name = "dashboard:skill_delete"
    search_fields = ["name", "proficiency"]
    columns = [
        {"name": "name", "label": "Name"},
        {"name": "proficiency", "label": "Proficiency"},
    ]


class SkillCreateView(DashboardCreateView):
    model = Skill
    form_class = SkillForm
    title = "Add Skill"
    success_url = reverse_lazy("dashboard:skill_list")
    cancel_url = "dashboard:skill_list"


class SkillUpdateView(DashboardUpdateView):
    model = Skill
    form_class = SkillForm
    title = "Edit Skill"
    success_url = reverse_lazy("dashboard:skill_list")
    cancel_url = "dashboard:skill_list"


class SkillDeleteView(DashboardDeleteView):
    model = Skill
    title = "Delete Skill"
    success_url = reverse_lazy("dashboard:skill_list")
    cancel_url = "dashboard:skill_list"


class ProjectListView(DashboardListView):
    model = Project
    title = "Projects"
    create_url_name = "dashboard:project_create"
    edit_url_name = "dashboard:project_edit"
    delete_url_name = "dashboard:project_delete"
    search_fields = ["title", "description", "category"]
    columns = [
        {"name": "image", "label": "Image", "type": "image"},
        {"name": "title", "label": "Title"},
        {"name": "category", "label": "Category"},
        {"name": "date_created", "label": "Created"},
    ]


class ProjectCreateView(DashboardCreateView):
    model = Project
    form_class = ProjectForm
    title = "Add Project"
    success_url = reverse_lazy("dashboard:project_list")
    cancel_url = "dashboard:project_list"


class ProjectUpdateView(DashboardUpdateView):
    model = Project
    form_class = ProjectForm
    title = "Edit Project"
    success_url = reverse_lazy("dashboard:project_list")
    cancel_url = "dashboard:project_list"


class ProjectDeleteView(DashboardDeleteView):
    model = Project
    title = "Delete Project"
    success_url = reverse_lazy("dashboard:project_list")
    cancel_url = "dashboard:project_list"


class ExperienceListView(DashboardListView):
    model = Experience
    title = "Experience"
    create_url_name = "dashboard:experience_create"
    edit_url_name = "dashboard:experience_edit"
    delete_url_name = "dashboard:experience_delete"
    search_fields = ["job_title", "company", "description"]
    columns = [
        {"name": "job_title", "label": "Role"},
        {"name": "company", "label": "Company"},
        {"name": "start_date", "label": "Start"},
        {"name": "end_date", "label": "End"},
    ]


class ExperienceCreateView(DashboardCreateView):
    model = Experience
    form_class = ExperienceForm
    title = "Add Experience"
    success_url = reverse_lazy("dashboard:experience_list")
    cancel_url = "dashboard:experience_list"


class ExperienceUpdateView(DashboardUpdateView):
    model = Experience
    form_class = ExperienceForm
    title = "Edit Experience"
    success_url = reverse_lazy("dashboard:experience_list")
    cancel_url = "dashboard:experience_list"


class ExperienceDeleteView(DashboardDeleteView):
    model = Experience
    title = "Delete Experience"
    success_url = reverse_lazy("dashboard:experience_list")
    cancel_url = "dashboard:experience_list"
