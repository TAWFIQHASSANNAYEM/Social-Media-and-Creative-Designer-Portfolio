from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    category = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=50) 
    
    def __str__(self):
        return self.name

class Experience(models.Model):
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.job_title} at {self.company}"


class SiteProfile(models.Model):
    brand_name = models.CharField(max_length=120, default="Studio Bloom")
    logo = models.ImageField(upload_to="branding/", blank=True, null=True)
    tagline = models.CharField(max_length=200, blank=True)
    hero_badge = models.CharField(max_length=120, blank=True)
    hero_title = models.CharField(max_length=200, default="Hi, I’m Iqra")
    hero_subtitle = models.TextField(blank=True)
    hero_card_title = models.CharField(max_length=120, blank=True)
    hero_card_body = models.TextField(blank=True)
    hero_image = models.ImageField(upload_to="profile/", blank=True, null=True)
    favicon = models.ImageField(upload_to="branding/", blank=True, null=True)
    favicon_url = models.URLField(blank=True)
    availability = models.CharField(max_length=120, blank=True)
    location = models.CharField(max_length=120, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    cta_primary_text = models.CharField(max_length=60, default="View my work")
    cta_primary_target = models.CharField(max_length=120, default="#work")
    cta_secondary_text = models.CharField(max_length=60, default="My skill stack")
    cta_secondary_target = models.CharField(max_length=120, default="#skills")
    footer_text = models.CharField(max_length=200, blank=True)
    header_cta_text = models.CharField(max_length=60, default="Let’s chat")
    header_cta_target = models.CharField(max_length=120, default="#contact")
    about_intro = models.TextField(blank=True)
    services_intro = models.TextField(blank=True)
    skills_intro = models.TextField(blank=True)
    work_intro = models.TextField(blank=True)
    experience_intro = models.TextField(blank=True)
    contact_intro = models.TextField(blank=True)
    features_intro = models.TextField(blank=True)
    seo_title = models.CharField(max_length=160, blank=True)
    seo_description = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand_name or "Site Profile"


class AboutCard(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Highlight(models.Model):
    value = models.CharField(max_length=40)
    label = models.CharField(max_length=120)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.value} - {self.label}"


class SocialLink(models.Model):
    label = models.CharField(max_length=80, blank=True)
    url = models.URLField()
    icon = models.CharField(max_length=80, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.label or self.url

    def save(self, *args, **kwargs):
        if not self.label and self.url:
            self.label = self._label_from_url(self.url)
        super().save(*args, **kwargs)

    @staticmethod
    def _label_from_url(url):
        try:
            host = url.replace("https://", "").replace("http://", "")
            host = host.split("/")[0].replace("www.", "")
        except Exception:
            return "Social"
        if "linkedin.com" in host:
            return "LinkedIn"
        if "instagram.com" in host:
            return "Instagram"
        if "facebook.com" in host:
            return "Facebook"
        if "behance.net" in host:
            return "Behance"
        if "dribbble.com" in host:
            return "Dribbble"
        if "youtube.com" in host:
            return "YouTube"
        if "tiktok.com" in host:
            return "TikTok"
        if "github.com" in host:
            return "GitHub"
        return "Social"


class Feature(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
