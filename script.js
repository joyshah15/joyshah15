/* Mobile Navigation Toggle */
const navToggle = document.getElementById('nav-toggle');
const navMenu = document.getElementById('nav-menu');

navToggle.addEventListener('click', () => {
  navMenu.querySelector('ul').classList.toggle('show');
  navToggle.classList.toggle('active');
});

/* Close navigation when a link is clicked (mobile) */
navMenu.addEventListener('click', (e) => {
  if (e.target.tagName === 'A') {
    navMenu.querySelector('ul').classList.remove('show');
    navToggle.classList.remove('active');
  }
});

/* Smooth Scroll for browsers that support Scroll Behavior */
const links = document.querySelectorAll('a[href^="#"]');

links.forEach(link => {
  link.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.hash);
    target?.scrollIntoView({ behavior: 'smooth' });
  });
});

/* Set current year in footer */
document.getElementById('year').textContent = new Date().getFullYear();