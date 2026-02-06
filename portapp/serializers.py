from rest_framework import serializers

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
    MediaAsset,
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "description",
            "image",
            "image_url",
            "category",
            "date_created",
            "url",
        ]
        read_only_fields = ["date_created"]


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["id", "name", "proficiency"]


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = [
            "id",
            "job_title",
            "company",
            "start_date",
            "end_date",
            "description",
        ]


class SiteProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteProfile
        fields = [
            "id",
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
            "updated_at",
        ]


class AboutCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCard
        fields = ["id", "title", "body", "order", "is_active"]


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["id", "title", "body", "order", "is_active"]


class HighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Highlight
        fields = ["id", "value", "label", "order", "is_active"]


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = ["id", "label", "url", "icon", "order", "is_active"]


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ["id", "title", "body", "order", "is_active"]


class MediaAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaAsset
        fields = ["id", "title", "image", "image_url", "notes", "created_at"]
