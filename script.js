// script.js - mobile menu toggle and active nav highlighting
document.addEventListener('DOMContentLoaded', function () {
  const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
  const navMenu = document.querySelector('nav ul');

  if (mobileMenuBtn && navMenu) {
    mobileMenuBtn.addEventListener('click', () => {
      navMenu.classList.toggle('active');
    });
  }

  // Highlight active nav link based on current URL
  const navLinks = document.querySelectorAll('nav ul li a');
  if (navLinks.length) {
    const path = window.location.pathname.split('/').pop().toLowerCase();
    navLinks.forEach(link => {
      const href = link.getAttribute('href') || '';
      if (href.toLowerCase() === path || (href === 'index.htm' && (path === '' || path === 'index.htm'))) {
        link.classList.add('active');
      } else {
        link.classList.remove('active');
      }
    });
  }
});
