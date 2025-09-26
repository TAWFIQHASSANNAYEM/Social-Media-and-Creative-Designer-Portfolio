from django.shortcuts import render, redirect
from portapp.models import *
from django.core.mail import send_mail
from portfolio.forms import ContactForm

def home(request):
    return render(request, 'home.html')

def about(request):
    experiences = Experience.objects.all().order_by('-start_date')
    skills = Skill.objects.all()
    personal_summary = "Creative and detail-oriented Social Media Manager and Content Designer with a strong record of producing high-volume, high-quality visuals for international clients. Skilled in Canva, CapCut, and cross-platform scheduling, consistently driving brand consistency and audience engagement. Currently finishing a B.Sc. in Computer Science & Engineering with research in AI-assisted patient referral systems."
    context = {
        'experiences': experiences,
        'skills': skills,
        'personal_summary': personal_summary
    }
    return render(request, 'about.html', context)


def portfolio(request):
    category = request.GET.get('category')
    projects = Project.objects.all().order_by('-id')
    
    if category:
        projects = projects.filter(category=category)
        
    categories = Project.objects.values_list('category', flat=True).distinct()
        
    context = {
        'projects': projects,
        'categories': categories,
        'selected_category': category
    }
    return render(request, 'portfolio.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
           
            send_mail(
                f'Message from {name} via portfolio',
                message,
                email,
                ['iqrayeafhy@gmail.com'], 
                fail_silently=False,
            )
            return redirect('home')
    else:
        form = ContactForm()
    
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)