from django.contrib import admin
from .models import Profile, Project, Skill, Experience, Contact, SiteConfiguration

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'title', 'email')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'featured', 'start_date', 'order')
    list_filter = ('status', 'featured', 'start_date')
    search_fields = ('title', 'description', 'technologies')
    list_editable = ('featured', 'order')
    ordering = ['-featured', 'order', '-start_date']
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'short_description', 'description', 'image')
        }),
        ('Technical Details', {
            'fields': ('technologies', 'github_url', 'live_url')
        }),
        ('Project Status', {
            'fields': ('status', 'start_date', 'end_date', 'featured', 'order')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'percentage', 'category', 'order')
    list_filter = ('level', 'category')
    search_fields = ('name', 'category')
    list_editable = ('level', 'percentage', 'order')
    ordering = ['order', 'name']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'type', 'current', 'start_date', 'end_date', 'order')
    list_filter = ('type', 'current', 'start_date')
    search_fields = ('title', 'company', 'description')
    list_editable = ('current', 'order')
    ordering = ['-current', 'order', '-start_date']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'replied')
    list_filter = ('replied', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_editable = ('replied',)
    readonly_fields = ('created_at',)
    ordering = ['-created_at']
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'subject')
        }),
        ('Message', {
            'fields': ('message',)
        }),
        ('Status', {
            'fields': ('replied', 'created_at')
        }),
    )

@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Allow only one site configuration
        return not SiteConfiguration.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    fieldsets = (
        ('Site Information', {
            'fields': ('site_title', 'site_description')
        }),
        ('Homepage Hero Section', {
            'fields': ('hero_title', 'hero_subtitle')
        }),
        ('Footer', {
            'fields': ('footer_text',)
        }),
        ('Analytics', {
            'fields': ('google_analytics_id',),
            'classes': ('collapse',)
        }),
    )
