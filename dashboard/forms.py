from django import forms

from portapp.models import (
    AboutCard,
    Experience,
    Feature,
    Highlight,
    MediaAsset,
    Project,
    Service,
    SiteProfile,
    Skill,
    SocialLink,
)


class StyledModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            widget = field.widget
            if isinstance(widget, forms.CheckboxInput):
                widget.attrs.setdefault("class", "h-4 w-4 rounded border-pink-300")
                continue
            base = (
                "w-full rounded-xl border border-pink-200 px-4 py-2 "
                "text-sm focus:border-pink-400 focus:outline-none"
            )
            existing = widget.attrs.get("class", "")
            widget.attrs["class"] = f"{base} {existing}".strip()
            if isinstance(widget, forms.Textarea):
                widget.attrs.setdefault("rows", 4)


class SiteProfileForm(StyledModelForm):
    class Meta:
        model = SiteProfile
        fields = [
            "brand_name",
            "logo",
            "logo_url",
            "tagline",
            "hero_badge",
            "hero_title",
            "hero_subtitle",
            "hero_card_title",
            "hero_card_body",
            "hero_image",
            "hero_image_url",
            "favicon",
            "favicon_url",
            "availability",
            "location",
            "email",
            "phone",
            "cta_primary_text",
            "cta_primary_target",
            "cta_secondary_text",
            "cta_secondary_target",
            "footer_text",
            "header_cta_text",
            "header_cta_target",
            "about_intro",
            "services_intro",
            "skills_intro",
            "work_intro",
            "experience_intro",
            "contact_intro",
            "features_intro",
            "show_education",
            "show_features",
            "show_services",
            "show_skills",
            "show_projects",
            "show_experience",
            "show_contact",
            "seo_title",
            "seo_description",
        ]


class AboutCardForm(StyledModelForm):
    class Meta:
        model = AboutCard
        fields = ["title", "body", "order", "is_active"]


class ServiceForm(StyledModelForm):
    class Meta:
        model = Service
        fields = ["title", "body", "order", "is_active"]


class HighlightForm(StyledModelForm):
    class Meta:
        model = Highlight
        fields = ["value", "label", "order", "is_active"]


class SocialLinkForm(StyledModelForm):
    class Meta:
        model = SocialLink
        fields = ["label", "url", "icon", "order", "is_active"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["label"].required = False
        self.fields["label"].help_text = "Optional. Leave blank to auto-detect from the URL."


class FeatureForm(StyledModelForm):
    class Meta:
        model = Feature
        fields = ["title", "body", "order", "is_active"]




class SkillForm(StyledModelForm):
    class Meta:
        model = Skill
        fields = ["name", "proficiency"]


class ProjectForm(StyledModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "image", "image_url", "category", "url"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 5}),
        }


class MediaAssetForm(StyledModelForm):
    class Meta:
        model = MediaAsset
        fields = ["title", "image", "image_url", "notes"]
        widgets = {
            "notes": forms.Textarea(attrs={"rows": 4}),
        }


class ExperienceForm(StyledModelForm):
    class Meta:
        model = Experience
        fields = ["job_title", "company", "start_date", "end_date", "description"]
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
            "description": forms.Textarea(attrs={"rows": 5}),
        }
