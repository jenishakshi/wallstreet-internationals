// ====================================
// WALL STREET INTERNATINOL - MAIN JAVASCRIPT
// ====================================

// Mobile Menu Toggle
document.addEventListener('DOMContentLoaded', function() {
  const menuToggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.nav');
  
  if (menuToggle) {
    menuToggle.addEventListener('click', function() {
      nav.classList.toggle('active');
      
      // Animate hamburger icon
      const spans = menuToggle.querySelectorAll('span');
      if (nav.classList.contains('active')) {
        spans[0].style.transform = 'rotate(45deg) translateY(8px)';
        spans[1].style.opacity = '0';
        spans[2].style.transform = 'rotate(-45deg) translateY(-8px)';
      } else {
        spans[0].style.transform = '';
        spans[1].style.opacity = '1';
        spans[2].style.transform = '';
      }
    });
  }
  
  // Set active navigation based on current page
  const currentPath = window.location.pathname;
  const navLinks = document.querySelectorAll('.nav-link');
  
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (currentPath === href || currentPath.endsWith(href)) {
      link.classList.add('active');
    }
  });
  
  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
  
  // Form validation
  const contactForm = document.querySelector('.contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
      e.preventDefault();
      
      const email = this.querySelector('input[type="email"]');
      const message = this.querySelector('textarea');
      
      // Basic validation
      if (!email.value || !message.value) {
        alert('Please fill in all required fields.');
        return;
      }
      
      // Email validation
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(email.value)) {
        alert('Please enter a valid email address.');
        return;
      }
      
      // Success message
      alert('Thank you for your message! We will get back to you soon.');
      this.reset();
    });
  }
  
  // Fade in elements on scroll
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };
  
  const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('fade-in');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);
  
  // Observe cards and feature boxes
  document.querySelectorAll('.card, .feature-box').forEach(el => {
    observer.observe(el);
  });
  
  // Add hover effect sound (optional - currently disabled)
  // Can be enabled by uncommenting the following code
  /*
  const cards = document.querySelectorAll('.card');
  cards.forEach(card => {
    card.addEventListener('mouseenter', function() {
      // Add subtle scale effect
      this.style.transform = 'translateY(-8px) scale(1.02)';
    });
    
    card.addEventListener('mouseleave', function() {
      this.style.transform = '';
    });
  });
  */
});

// Utility function to load external HTML (for components)
async function loadComponent(elementId, filePath) {
  try {
    const response = await fetch(filePath);
    const html = await response.text();
    document.getElementById(elementId).innerHTML = html;
  } catch (error) {
    console.error('Error loading component:', error);
  }
}

// Back to top button (can be added to footer)
function scrollToTop() {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
}
