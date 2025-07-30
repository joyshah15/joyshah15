from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('contact/', views.contact, name='contact'),
    path('contact/ajax/', views.contact_ajax, name='contact_ajax'),
    path('resume/', views.resume_download, name='resume_download'),
]