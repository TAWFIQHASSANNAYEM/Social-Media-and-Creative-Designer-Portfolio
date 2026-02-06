from django.contrib import admin
from portapp.models import (
    AboutCard,
    Category,
    Experience,
    Highlight,
    Project,
    Service,
    SiteProfile,
    Skill,
    SocialLink,
    Feature,
)

admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(SiteProfile)
admin.site.register(AboutCard)
admin.site.register(Service)
admin.site.register(Highlight)
admin.site.register(SocialLink)
admin.site.register(Feature)

