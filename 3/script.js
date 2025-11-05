// ----------------------------
// script.js — TKS Bahrain Clone
// ----------------------------

// Mobile menu toggle
const menuBtn = document.getElementById('menuBtn');
const mainNav = document.getElementById('mainNav');

if (menuBtn) {
  menuBtn.addEventListener('click', () => {
    if (mainNav.style.display === 'flex') {
      mainNav.style.display = 'none';
    } else {
      mainNav.style.display = 'flex';
      mainNav.style.flexDirection = 'column';
      mainNav.style.gap = '10px';
      mainNav.style.background = '#fff';
      mainNav.style.padding = '10px';
      mainNav.style.border = '1px solid #eee';
      mainNav.style.borderRadius = '10px';
    }
  });
}

// Contact form handler
document.getElementById('contactForm').addEventListener('submit', function (e) {
  e.preventDefault();
  const name = document.getElementById('name').value;
  alert(`Thanks ${name}! Your message has been received (demo).`);
  this.reset();
});

// Register form handler
document.getElementById('registerForm').addEventListener('submit', function (e) {
  e.preventDefault();
  const rname = document.getElementById('rname').value;
  alert(`Thank you for registering, ${rname}! (demo)`);
  this.reset();
});

// Donate button
const donateBtn = document.getElementById('donateBtn');
if (donateBtn) {
  donateBtn.addEventListener('click', function () {
    alert('Donate flow not implemented in this demo.');
  });
}
