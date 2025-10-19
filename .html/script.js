// Basic interactive behavior: mobile nav, slider, contact submit
document.addEventListener('DOMContentLoaded', function () {
  // nav toggle
  const navToggle = document.getElementById('nav-toggle');
  const mainNav = document.getElementById('main-nav');
  navToggle.addEventListener('click', () => {
    const expanded = navToggle.getAttribute('aria-expanded') === 'true';
    navToggle.setAttribute('aria-expanded', String(!expanded));
    mainNav.classList.toggle('open');
  });

  // simple slider
  const slider = document.querySelector('.hero-slider');
  if (slider) {
    const slides = Array.from(slider.querySelectorAll('.slide'));
    const prevBtn = slider.querySelector('.prev');
    const nextBtn = slider.querySelector('.next');
    let current = slides.findIndex(s => s.classList.contains('active')) || 0;
    const interval = parseInt(slider.dataset.interval || 5000, 10);
    let timer = null;

    function showSlide(i) {
      slides.forEach((s, idx) => s.classList.toggle('active', idx === i));
      current = i;
    }
    function next() { showSlide((current + 1) % slides.length); }
    function prev() { showSlide((current - 1 + slides.length) % slides.length); }

    if (nextBtn) nextBtn.addEventListener('click', () => { next(); resetTimer(); });
    if (prevBtn) prevBtn.addEventListener('click', () => { prev(); resetTimer(); });

    function startTimer() {
      if (slider.dataset.autoplay === 'true') {
        timer = setInterval(next, interval);
      }
    }
    function resetTimer() {
      if (timer) { clearInterval(timer); startTimer(); }
    }
    startTimer();
  }

  // contact form simple client validation / fake submit
  const contactForm = document.getElementById('contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const formData = new FormData(contactForm);
      const name = formData.get('name')?.toString().trim();
      const email = formData.get('email')?.toString().trim();
      const message = formData.get('message')?.toString().trim();
      if (!name || !email || !message) {
        alert('Please fill in Name, Email and Message.');
        return;
      }
      // Here you would send to your server via fetch()
      alert('Thank you — your message has been received (demo).');
      contactForm.reset();
    });
  }
});