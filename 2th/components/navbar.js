class CustomFooter extends HTMLElement {
  connectedCallback() {
    this.attachShadow({ mode: 'open' });
    this.shadowRoot.innerHTML = `
      <style>
        footer {
          background-color: #1A202C;
          color: white;
          padding: 3rem 2rem;
        }
        .footer-container {
          max-width: 1200px;
          margin: 0 auto;
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
          gap: 2rem;
        }
        .footer-logo {
          font-size: 1.5rem;
          font-weight: bold;
          margin-bottom: 1rem;
          display: flex;
          align-items: center;
          gap: 0.5rem;
        }
        .footer-logo-icon {
          color: #FF6B35;
        }
        .footer-description {
          color: #CBD5E0;
          margin-bottom: 1.5rem;
          line-height: 1.6;
        }
        .footer-links h3 {
          font-size: 1.125rem;
          font-weight: 600;
          margin-bottom: 1.5rem;
          color: white;
        }
        .footer-links ul {
          list-style: none;
          padding: 0;
          margin: 0;
        }
        .footer-links li {
          margin-bottom: 0.75rem;
        }
        .footer-links a {
          color: #CBD5E0;
          text-decoration: none;
          transition: color 0.3s ease;
        }
        .footer-links a:hover {
          color: #FF6B35;
        }
        .social-links {
          display: flex;
          gap: 1rem;
          margin-top: 1rem;
        }
        .social-links a {
          color: white;
          background-color: rgba(255, 255, 255, 0.1);
          width: 40px;
          height: 40px;
          border-radius: 50%;
          display: flex;
          align-items: center;
          justify-content: center;
          transition: background-color 0.3s ease;
        }
        .social-links a:hover {
          background-color: #FF6B35;
        }
        .copyright {
          text-align: center;
          padding-top: 2rem;
          margin-top: 2rem;
          border-top: 1px solid rgba(255, 255, 255, 0.1);
          color: #CBD5E0;
          font-size: 0.875rem;
        }
      </style>
      <footer>
        <div class="footer-container">
          <div class="footer-about">
            <div class="footer-logo">
              <i data-feather="cpu" class="footer-logo-icon"></i>
              TKS Bahrain
            </div>
            <p class="footer-description">
              The Knowledge Society of Bahrain fostering innovation and technological advancement in the region.
            </p>
            <div class="social-links">
              <a href="#"><i data-feather="facebook"></i></a>
              <a href="#"><i data-feather="twitter"></i></a>
              <a href="#"><i data-feather="linkedin"></i></a>
              <a href="#"><i data-feather="instagram"></i></a>
            </div>
          </div>
          <div class="footer-links">
            <h3>Quick Links</h3>
            <ul>
              <li><a href="/">Home</a></li>
              <li><a href="#about">About Us</a></li>
              <li><a href="#programs">Our Programs</a></li>
              <li><a href="#events">Events</a></li>
              <li><a href="#contact">Contact</a></li>
            </ul>
          </div>
          <div class="footer-links">
            <h3>Programs</h3>
            <ul>
              <li><a href="#">Education</a></li>
              <li><a href="#">Networking</a></li>
              <li><a href="#">Recognition</a></li>
              <li><a href="#">Research</a></li>
              <li><a href="#">Workshops</a></li>
            </ul>
          </div>
          <div class="footer-links">
            <h3>Contact</h3>
            <ul>
              <li><a href="mailto:info@tksbahrain.com">info@tksbahrain.com</a></li>
              <li><a href="tel:+97312345678">+973 1234 5678</a></li>
              <li>123 Knowledge Avenue</li>
              <li>Manama, Bahrain</li>
            </ul>
          </div>
        </div>
        <div class="copyright">
          &copy; ${new Date().getFullYear()} The Knowledge Society Bahrain. All rights reserved.
        </div>
      </footer>
      <script>feather.replace();</script>
    `;
  }
}
customElements.define('custom-footer', CustomFooter);