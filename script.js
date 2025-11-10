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
  
  // Submenu toggle handling (for mobile) and submenu active-state detection
  const submenuToggles = document.querySelectorAll('.submenu-toggle');
  submenuToggles.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const li = btn.closest('.has-submenu');
      if (!li) return;
      const isOpen = li.classList.toggle('open');
      btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
  });

  // Enhanced active highlighting for submenu links (match query params too)
  const allLinks = document.querySelectorAll('nav ul li a');
  const currentPath = window.location.pathname.split('/').pop().toLowerCase();
  const currentSearch = window.location.search.toLowerCase();
  allLinks.forEach(link => {
    try {
      const url = new URL(link.getAttribute('href'), window.location.origin);
      const linkFile = url.pathname.split('/').pop().toLowerCase();
      const linkSearch = url.search.toLowerCase();
      if (linkFile === currentPath && linkSearch === currentSearch) {
        link.classList.add('active');
        // also mark parent menu item active (for Services parent)
        const parent = link.closest('.has-submenu');
        if (parent) {
          const parentLink = parent.querySelector('.nav-link');
          if (parentLink) parentLink.classList.add('active');
        }
      }
    } catch (err) {
      // ignore malformed hrefs
    }
  });
});
