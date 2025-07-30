from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Profile, Project, Skill, Experience, Contact, SiteConfiguration
from .forms import ContactForm

def get_site_config():
    """Get or create site configuration"""
    config, created = SiteConfiguration.objects.get_or_create(
        pk=1,
        defaults={
            'site_title': 'My Portfolio',
            'site_description': 'Professional Portfolio Website',
            'hero_title': 'Welcome to My Portfolio',
            'hero_subtitle': 'I create amazing digital experiences',
            'footer_text': '© 2024 My Portfolio. All rights reserved.'
        }
    )
    return config

def home(request):
    """Homepage view with hero section and featured projects"""
    context = {
        'site_config': get_site_config(),
        'profile': Profile.objects.first(),
        'featured_projects': Project.objects.filter(featured=True)[:3],
        'skills': Skill.objects.all()[:8],  # Show top 8 skills on homepage
        'recent_experience': Experience.objects.filter(type='work')[:2],
    }
    return render(request, 'portfolio/home.html', context)

def about(request):
    """About page with profile information and experience"""
    context = {
        'site_config': get_site_config(),
        'profile': Profile.objects.first(),
        'work_experience': Experience.objects.filter(type='work'),
        'education': Experience.objects.filter(type='education'),
        'skills': Skill.objects.all(),
    }
    return render(request, 'portfolio/about.html', context)

def portfolio(request):
    """Portfolio page with all projects"""
    projects = Project.objects.all()
    
    # Filter by status if provided
    status_filter = request.GET.get('status')
    if status_filter and status_filter in ['completed', 'in_progress', 'planned']:
        projects = projects.filter(status=status_filter)
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        projects = projects.filter(
            title__icontains=search_query
        ).union(
            projects.filter(description__icontains=search_query)
        ).union(
            projects.filter(technologies__icontains=search_query)
        )
    
    context = {
        'site_config': get_site_config(),
        'projects': projects,
        'search_query': search_query,
        'status_filter': status_filter,
    }
    return render(request, 'portfolio/portfolio.html', context)

def project_detail(request, project_id):
    """Project detail page"""
    project = get_object_or_404(Project, id=project_id)
    related_projects = Project.objects.exclude(id=project_id)[:3]
    
    context = {
        'site_config': get_site_config(),
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'portfolio/project_detail.html', context)

def contact(request):
    """Contact page with contact form"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the contact message
            contact_message = form.save()
            
            # Send email notification (optional)
            try:
                profile = Profile.objects.first()
                if profile and profile.email:
                    send_mail(
                        subject=f'New Portfolio Contact: {contact_message.subject}',
                        message=f'''
                        New contact message from your portfolio website:
                        
                        Name: {contact_message.name}
                        Email: {contact_message.email}
                        Subject: {contact_message.subject}
                        
                        Message:
                        {contact_message.message}
                        ''',
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[profile.email],
                        fail_silently=True,
                    )
            except Exception as e:
                pass  # Email sending is optional
            
            messages.success(request, 'Thank you for your message! I\'ll get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    context = {
        'site_config': get_site_config(),
        'profile': Profile.objects.first(),
        'form': form,
    }
    return render(request, 'portfolio/contact.html', context)

@csrf_exempt
def contact_ajax(request):
    """AJAX endpoint for contact form submission"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            return JsonResponse({
                'success': True,
                'message': 'Thank you for your message! I\'ll get back to you soon.'
            })
        else:
            return JsonResponse({
                'success': False,
                'errors': form.errors
            })
    return JsonResponse({'success': False, 'message': 'Invalid request method'})

def resume_download(request):
    """Handle resume download"""
    profile = Profile.objects.first()
    if profile and profile.resume_file:
        response = FileResponse(
            profile.resume_file.open('rb'),
            content_type='application/pdf',
            as_attachment=True,
            filename=f'{profile.name}_Resume.pdf'
        )
        return response
    else:
        messages.error(request, 'Resume not available for download.')
        return redirect('about')
