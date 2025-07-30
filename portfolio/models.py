from django.db import models
from django.utils import timezone

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    resume_file = models.FileField(upload_to='resume/', blank=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

class Skill(models.Model):
    SKILL_LEVELS = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ]
    
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=20, choices=SKILL_LEVELS, default='intermediate')
    percentage = models.IntegerField(default=75, help_text="Skill level percentage (0-100)")
    category = models.CharField(max_length=100, help_text="e.g., Programming, Design, Tools")
    order = models.IntegerField(default=0, help_text="Order for display")
    
    def __str__(self):
        return f"{self.name} ({self.level})"
    
    class Meta:
        ordering = ['order', 'name']

class Project(models.Model):
    PROJECT_STATUS = [
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
        ('planned', 'Planned'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    short_description = models.CharField(max_length=300, help_text="Brief description for cards")
    image = models.ImageField(upload_to='projects/', blank=True)
    technologies = models.CharField(max_length=500, help_text="Comma-separated list of technologies")
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    status = models.CharField(max_length=20, choices=PROJECT_STATUS, default='completed')
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    featured = models.BooleanField(default=False, help_text="Feature this project on homepage")
    order = models.IntegerField(default=0, help_text="Order for display")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_technologies_list(self):
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]
    
    class Meta:
        ordering = ['-featured', 'order', '-start_date']

class Experience(models.Model):
    EXPERIENCE_TYPE = [
        ('work', 'Work Experience'),
        ('education', 'Education'),
        ('volunteer', 'Volunteer'),
        ('freelance', 'Freelance'),
    ]
    
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=EXPERIENCE_TYPE, default='work')
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    current = models.BooleanField(default=False, help_text="Currently working here")
    order = models.IntegerField(default=0, help_text="Order for display")
    
    def __str__(self):
        return f"{self.title} at {self.company}"
    
    class Meta:
        ordering = ['-current', 'order', '-start_date']

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    replied = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
    
    class Meta:
        ordering = ['-created_at']

class SiteConfiguration(models.Model):
    site_title = models.CharField(max_length=100, default="My Portfolio")
    site_description = models.TextField(default="Professional Portfolio Website")
    hero_title = models.CharField(max_length=200, default="Welcome to My Portfolio")
    hero_subtitle = models.CharField(max_length=300, default="I create amazing digital experiences")
    footer_text = models.CharField(max_length=200, default="© 2024 My Portfolio. All rights reserved.")
    google_analytics_id = models.CharField(max_length=50, blank=True, help_text="Google Analytics tracking ID")
    
    def __str__(self):
        return "Site Configuration"
    
    class Meta:
        verbose_name = "Site Configuration"
        verbose_name_plural = "Site Configuration"
