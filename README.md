# Portfolio Website - Django

A modern, responsive portfolio website built with Django and Bootstrap 5. This website showcases projects, skills, experience, and provides a contact form for potential clients or employers.

## Features

### 🎨 Modern Design
- Responsive design that works on all devices
- Beautiful animations with AOS (Animate On Scroll)
- Bootstrap 5 for modern UI components
- Custom CSS with gradient backgrounds and smooth transitions

### 📊 Portfolio Management
- **Projects**: Showcase your work with images, descriptions, and technology stacks
- **Skills**: Display your technical skills with progress bars and categories
- **Experience**: Timeline view of work experience and education
- **Profile**: Personal information and contact details

### 🔧 Admin Interface
- Fully configured Django admin for easy content management
- Custom admin interfaces for all models
- Bulk editing capabilities for projects and skills
- Image upload support for profile and project images

### 📧 Contact System
- Contact form with validation
- Email notifications for new messages
- AJAX form submission for better UX
- FAQ section for common questions

### 🚀 Performance & SEO
- Optimized for search engines
- Fast loading with lazy image loading
- Google Analytics integration
- Social media sharing buttons

## Project Structure

```
portfolio_site/
├── portfolio/                 # Main Django app
│   ├── models.py             # Database models
│   ├── views.py              # View functions
│   ├── forms.py              # Contact form
│   ├── admin.py              # Admin configuration
│   └── urls.py               # URL patterns
├── templates/portfolio/       # HTML templates
│   ├── base.html             # Base template
│   ├── home.html             # Homepage
│   ├── about.html            # About page
│   ├── portfolio.html        # Portfolio page
│   ├── project_detail.html   # Project detail page
│   └── contact.html          # Contact page
├── static/                   # Static files
│   ├── css/style.css         # Custom CSS
│   └── js/main.js            # Custom JavaScript
├── media/                    # Uploaded files
├── portfolio_site/           # Django project settings
│   ├── settings.py           # Project settings
│   └── urls.py               # Main URL configuration
├── manage.py                 # Django management script
└── requirements.txt          # Python dependencies
```

## Models

### Profile
- Personal information (name, title, bio, contact info)
- Social media links (GitHub, LinkedIn, Twitter)
- Profile image and resume file upload

### Project
- Project details (title, description, images)
- Technology stack and project status
- GitHub and live demo links
- Featured project highlighting

### Skill
- Skill name, level, and percentage
- Category grouping for organization
- Custom ordering for display

### Experience
- Work experience and education
- Company, title, and date ranges
- Current position indicator
- Custom descriptions

### Contact
- Contact form submissions
- Message tracking and status
- Email notifications

### SiteConfiguration
- Global site settings
- Hero section content
- Analytics integration
- Footer customization

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

### Step 1: Clone or Download
```bash
# If you have the project files, navigate to the directory
cd portfolio_site
```

### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python3 -m venv portfolio_env

# Activate virtual environment
# On Linux/Mac:
source portfolio_env/bin/activate
# On Windows:
portfolio_env\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Database Setup
```bash
# Apply database migrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser
```

### Step 5: Collect Static Files (Production)
```bash
python manage.py collectstatic
```

### Step 6: Run Development Server
```bash
python manage.py runserver
```

The website will be available at `http://localhost:8000`

## Configuration

### Admin Access
- Visit `http://localhost:8000/admin`
- Login with the superuser credentials you created
- Add your profile information, projects, skills, and experience

### Required Setup Steps
1. **Create Profile**: Add your personal information in the admin
2. **Add Skills**: Create skills with categories and levels
3. **Add Projects**: Upload your projects with images and descriptions
4. **Add Experience**: Include work experience and education
5. **Configure Site**: Update site configuration for hero section

### Optional Configuration
- **Email Settings**: Configure email backend for contact form notifications
- **Google Analytics**: Add your Google Analytics tracking ID
- **Social Media**: Add your social media profile links
- **Custom Domain**: Configure for production deployment

## Customization

### Styling
- Edit `static/css/style.css` for custom styles
- Modify color scheme in CSS variables at the top of the file
- Customize Bootstrap components in templates

### Content
- Update templates in `templates/portfolio/` directory
- Modify text content and layout as needed
- Add new sections or pages by creating new views and templates

### Functionality
- Extend models in `portfolio/models.py` for additional fields
- Add new views in `portfolio/views.py` for custom pages
- Customize admin interface in `portfolio/admin.py`

## Deployment

### Production Settings
1. Set `DEBUG = False` in `settings.py`
2. Configure `ALLOWED_HOSTS` with your domain
3. Set up a production database (PostgreSQL recommended)
4. Configure email backend for contact form
5. Set up static file serving (nginx + gunicorn recommended)

### Environment Variables
Create a `.env` file for sensitive settings:
```
SECRET_KEY=your-secret-key
DEBUG=False
DATABASE_URL=your-database-url
EMAIL_HOST=your-email-host
EMAIL_HOST_USER=your-email
EMAIL_HOST_PASSWORD=your-password
```

## Technologies Used

### Backend
- **Django 5.2.4**: Web framework
- **Python 3.13**: Programming language
- **SQLite**: Database (development)
- **Pillow**: Image processing

### Frontend
- **Bootstrap 5.3.2**: CSS framework
- **Font Awesome 6.4.0**: Icons
- **AOS 2.3.1**: Scroll animations
- **Google Fonts**: Typography (Inter)

### Features
- Responsive design
- Modern animations
- Contact form with validation
- Admin interface for content management
- Image upload support
- SEO optimized

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For questions or issues:
1. Check the Django documentation: https://docs.djangoproject.com/
2. Review the Bootstrap documentation: https://getbootstrap.com/docs/
3. Check the code comments for implementation details

## Default Admin Credentials

For testing purposes, a default superuser has been created:
- **Username**: admin
- **Email**: admin@example.com
- **Password**: admin123

**⚠️ Important**: Change these credentials before deploying to production!

## Next Steps

1. **Add Content**: Use the admin interface to add your personal information
2. **Customize Design**: Modify colors and layout to match your brand
3. **Add Projects**: Upload your best work with detailed descriptions
4. **Configure Email**: Set up email for contact form notifications
5. **Deploy**: Choose a hosting platform and deploy your site

---

Happy coding! 🚀
