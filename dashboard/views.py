from django.shortcuts import render
from portapp.models import *
from hitcount.models import HitCount

def owner_dashboard(request):
    total_projects = Project.objects.count()
    total_experiences = Experience.objects.count()
    total_skills = Skill.objects.count()

    # Get the total hits for the homepage
    try:
        total_hits = HitCount.objects.get(pk=1).hits
    except HitCount.DoesNotExist:
        total_hits = 0

    context = {
        'total_projects': total_projects,
        'total_experiences': total_experiences,
        'total_skills': total_skills,
        'total_hits': total_hits,  # Add this line

    }
    return render(request, 'dashboard/dashboard.html', context)

