// Portfolio Website JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Initialize AOS (Animate On Scroll)
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            easing: 'ease-in-out',
            once: true,
            offset: 100
        });
    }
    
    // Scroll to Top Button
    initScrollToTop();
    
    // Navbar transparency on scroll
    initNavbarScroll();
    
    // Smooth scrolling for anchor links
    initSmoothScrolling();
    
    // Typing animation for hero section
    initTypingAnimation();
    
    // Progress bar animations
    initProgressBars();
    
    // Contact form handling
    initContactForm();
    
    // Project filter animations
    initProjectFilters();
    
    // Lazy loading for images
    initLazyLoading();
});

// Scroll to Top Button
function initScrollToTop() {
    const scrollToTopBtn = document.getElementById('scrollToTop');
    if (!scrollToTopBtn) return;
    
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            scrollToTopBtn.classList.add('show');
        } else {
            scrollToTopBtn.classList.remove('show');
        }
    });
    
    scrollToTopBtn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

// Navbar Background on Scroll
function initNavbarScroll() {
    const navbar = document.querySelector('.navbar');
    if (!navbar) return;
    
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 50) {
            navbar.classList.add('scrolled');
            navbar.style.backgroundColor = 'rgba(52, 58, 64, 0.95)';
        } else {
            navbar.classList.remove('scrolled');
            navbar.style.backgroundColor = 'rgba(52, 58, 64, 0.9)';
        }
    });
}

// Smooth Scrolling for Anchor Links
function initSmoothScrolling() {
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href === '#') return;
            
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                const offsetTop = target.offsetTop - 80; // Account for fixed navbar
                
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// Typing Animation for Hero Section
function initTypingAnimation() {
    const typingElement = document.querySelector('.typing-animation');
    if (!typingElement) return;
    
    const texts = typingElement.dataset.texts ? typingElement.dataset.texts.split(',') : [];
    if (texts.length === 0) return;
    
    let textIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    
    function typeWriter() {
        const currentText = texts[textIndex];
        
        if (isDeleting) {
            typingElement.textContent = currentText.substring(0, charIndex - 1);
            charIndex--;
        } else {
            typingElement.textContent = currentText.substring(0, charIndex + 1);
            charIndex++;
        }
        
        let typeSpeed = isDeleting ? 50 : 100;
        
        if (!isDeleting && charIndex === currentText.length) {
            typeSpeed = 2000; // Pause at end
            isDeleting = true;
        } else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            textIndex = (textIndex + 1) % texts.length;
            typeSpeed = 500; // Pause before next text
        }
        
        setTimeout(typeWriter, typeSpeed);
    }
    
    typeWriter();
}

// Progress Bar Animations
function initProgressBars() {
    const progressBars = document.querySelectorAll('.progress-bar');
    
    const animateProgressBar = (progressBar) => {
        const targetWidth = progressBar.style.width;
        progressBar.style.width = '0%';
        
        setTimeout(() => {
            progressBar.style.width = targetWidth;
        }, 200);
    };
    
    // Intersection Observer for progress bars
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const progressBar = entry.target.querySelector('.progress-bar');
                if (progressBar) {
                    animateProgressBar(progressBar);
                }
            }
        });
    }, { threshold: 0.5 });
    
    document.querySelectorAll('.skill-item').forEach(skill => {
        observer.observe(skill);
    });
}

// Contact Form Handling
function initContactForm() {
    const contactForm = document.getElementById('contactForm');
    if (!contactForm) return;
    
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const formData = new FormData(this);
        const submitBtn = this.querySelector('button[type="submit"]');
        const originalText = submitBtn.innerHTML;
        
        // Show loading state
        submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Sending...';
        submitBtn.disabled = true;
        
        // Simulate form submission (replace with actual AJAX call)
        fetch(this.action || '/contact/ajax/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                showAlert('success', data.message || 'Message sent successfully!');
                contactForm.reset();
            } else {
                showAlert('error', data.message || 'There was an error sending your message.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            showAlert('error', 'There was an error sending your message.');
        })
        .finally(() => {
            // Restore button state
            submitBtn.innerHTML = originalText;
            submitBtn.disabled = false;
        });
    });
}

// Project Filter Animations
function initProjectFilters() {
    const filterButtons = document.querySelectorAll('.filter-buttons .btn');
    const projectCards = document.querySelectorAll('.project-card');
    
    filterButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (this.href && this.href.includes('?')) {
                return; // Let the link work normally for URL filters
            }
            
            e.preventDefault();
            
            // Update active button
            filterButtons.forEach(btn => btn.classList.remove('btn-primary'));
            filterButtons.forEach(btn => btn.classList.add('btn-outline-primary'));
            this.classList.remove('btn-outline-primary');
            this.classList.add('btn-primary');
            
            // Get filter value
            const filter = this.dataset.filter || 'all';
            
            // Animate cards
            projectCards.forEach((card, index) => {
                const shouldShow = filter === 'all' || card.dataset.category === filter;
                
                setTimeout(() => {
                    if (shouldShow) {
                        card.style.display = 'block';
                        card.style.animation = 'fadeInUp 0.5s ease forwards';
                    } else {
                        card.style.animation = 'fadeOut 0.3s ease forwards';
                        setTimeout(() => {
                            card.style.display = 'none';
                        }, 300);
                    }
                }, index * 50);
            });
        });
    });
}

// Lazy Loading for Images
function initLazyLoading() {
    const images = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                observer.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
}

// Alert System
function showAlert(type, message) {
    const alertContainer = document.getElementById('alert-container') || createAlertContainer();
    
    const alertElement = document.createElement('div');
    alertElement.className = `alert alert-${type === 'error' ? 'danger' : type} alert-dismissible fade show`;
    alertElement.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    alertContainer.appendChild(alertElement);
    
    // Auto-dismiss after 5 seconds
    setTimeout(() => {
        if (alertElement.parentNode) {
            alertElement.classList.remove('show');
            setTimeout(() => {
                alertElement.remove();
            }, 150);
        }
    }, 5000);
}

function createAlertContainer() {
    const container = document.createElement('div');
    container.id = 'alert-container';
    container.style.position = 'fixed';
    container.style.top = '90px';
    container.style.right = '20px';
    container.style.zIndex = '9999';
    container.style.maxWidth = '400px';
    document.body.appendChild(container);
    return container;
}

// Utility Functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// Performance optimization
const debouncedResize = debounce(() => {
    // Handle resize events
    if (typeof AOS !== 'undefined') {
        AOS.refresh();
    }
}, 250);

window.addEventListener('resize', debouncedResize);

// Add fade-out animation for page transitions
window.addEventListener('beforeunload', function() {
    document.body.style.opacity = '0';
    document.body.style.transition = 'opacity 0.3s ease';
});

// Error handling for missing elements
window.addEventListener('error', function(e) {
    console.error('JavaScript error:', e.error);
});

// Analytics (if Google Analytics is present)
function trackEvent(action, category, label) {
    if (typeof gtag !== 'undefined') {
        gtag('event', action, {
            event_category: category,
            event_label: label
        });
    }
}

// Export functions for use in other scripts
window.portfolioJS = {
    showAlert,
    trackEvent,
    debounce,
    throttle
};