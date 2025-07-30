# Modern Portfolio Website

A beautiful, responsive portfolio website built with HTML, CSS, and JavaScript. Features modern design, smooth animations, and mobile-first responsive layout.

## 🚀 Features

- **Modern Design**: Clean, professional design with gradient backgrounds and glassmorphism effects
- **Responsive Layout**: Fully responsive design that works on all devices
- **Smooth Animations**: CSS animations and JavaScript-powered interactions
- **Mobile Navigation**: Hamburger menu for mobile devices
- **Contact Form**: Functional contact form with validation
- **Scroll Animations**: Elements fade in as you scroll
- **Interactive Elements**: Hover effects and tilt animations
- **SEO Optimized**: Semantic HTML structure
- **Fast Loading**: Optimized for performance

## 📁 File Structure

```
portfolio/
├── index.html          # Main HTML file
├── styles.css          # CSS styles and animations
├── script.js           # JavaScript functionality
└── README.md           # This file
```

## 🛠️ Setup Instructions

1. **Download or Clone**: Get all the files in a folder
2. **Open in Browser**: Simply open `index.html` in your web browser
3. **Local Server** (Optional): For better development experience, use a local server:
   ```bash
   # Using Python
   python -m http.server 8000
   
   # Using Node.js
   npx serve .
   
   # Using PHP
   php -S localhost:8000
   ```

## 🎨 Customization Guide

### Personal Information

Edit the following sections in `index.html`:

#### Hero Section
```html
<h1 class="hero-title">
    Hi, I'm <span class="highlight">Your Name</span>
</h1>
<p class="hero-subtitle">Full Stack Developer & Creative Problem Solver</p>
```

#### About Section
```html
<p>I'm a passionate developer with a love for creating meaningful digital experiences...</p>
```

#### Contact Information
```html
<span>your.email@example.com</span>
<span>+1 (555) 123-4567</span>
<span>Your City, Country</span>
```

#### Social Links
```html
<a href="https://github.com/yourusername" class="social-link">
    <i class="fab fa-github"></i>
</a>
<a href="https://linkedin.com/in/yourusername" class="social-link">
    <i class="fab fa-linkedin"></i>
</a>
```

### Skills Section

Add or modify skills in the skills section:

```html
<div class="skill-item">
    <i class="fab fa-react"></i>
    <span>React</span>
</div>
```

### Projects Section

Update project information:

```html
<div class="project-card">
    <div class="project-image">
        <i class="fas fa-laptop-code"></i>
    </div>
    <div class="project-content">
        <h3>Your Project Name</h3>
        <p>Project description...</p>
        <div class="project-tech">
            <span>React</span>
            <span>Node.js</span>
        </div>
        <div class="project-links">
            <a href="https://your-project.com" class="project-link">
                <i class="fas fa-external-link-alt"></i> Live Demo
            </a>
            <a href="https://github.com/yourusername/project" class="project-link">
                <i class="fab fa-github"></i> Code
            </a>
        </div>
    </div>
</div>
```

### Colors and Styling

Main colors are defined in `styles.css`. You can customize:

- **Primary Color**: `#2563eb` (Blue)
- **Secondary Color**: `#667eea` (Purple)
- **Background Colors**: Various shades of gray
- **Gradients**: Hero section and accent elements

### Fonts

The website uses Inter font from Google Fonts. To change:

1. Update the Google Fonts link in `index.html`
2. Modify the font-family in `styles.css`

## 📱 Responsive Breakpoints

- **Desktop**: 1200px and above
- **Tablet**: 768px - 1199px
- **Mobile**: Below 768px
- **Small Mobile**: Below 480px

## 🎯 Features in Detail

### Navigation
- Fixed navigation bar with blur effect
- Smooth scrolling to sections
- Active link highlighting
- Mobile hamburger menu

### Hero Section
- Gradient background with animated elements
- Typing animation for title
- Floating profile card
- Call-to-action buttons

### About Section
- Statistics cards with hover effects
- Animated icons
- Responsive grid layout

### Skills Section
- Categorized skills display
- Icon-based skill representation
- Hover animations

### Projects Section
- Card-based project display
- Technology tags
- Live demo and code links
- 3D tilt effect on hover

### Contact Section
- Contact information with icons
- Social media links
- Functional contact form with validation
- Success/error notifications

### Animations
- Scroll-triggered fade-in animations
- Hover effects on interactive elements
- Smooth transitions throughout
- Loading animations

## 🔧 JavaScript Features

- **Mobile Navigation**: Toggle hamburger menu
- **Smooth Scrolling**: Navigation link functionality
- **Scroll Effects**: Navbar background change, parallax
- **Form Validation**: Contact form with email validation
- **Notifications**: Success/error message system
- **Animations**: Intersection Observer for scroll animations
- **Interactive Effects**: Tilt effects, hover animations

## 🌐 Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## 📈 Performance

- Optimized CSS with efficient selectors
- Minimal JavaScript for better performance
- Compressed images and assets
- Fast loading times

## 🚀 Deployment

### GitHub Pages
1. Create a new repository
2. Upload all files
3. Go to Settings > Pages
4. Select source branch (usually main)
5. Your site will be available at `https://username.github.io/repository-name`

### Netlify
1. Drag and drop the folder to Netlify
2. Your site will be deployed instantly
3. Get a custom domain if needed

### Vercel
1. Connect your GitHub repository
2. Vercel will automatically deploy
3. Get a custom domain and SSL

## 🤝 Contributing

Feel free to fork this project and customize it for your needs. If you make improvements, consider sharing them!

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you need help customizing your portfolio or have questions, feel free to reach out!

---

**Happy coding! 🎉**
