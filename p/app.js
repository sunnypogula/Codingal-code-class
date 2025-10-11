// app.js

document.addEventListener('DOMContentLoaded', () => {
       // --- Product Data ---
const products500g = [
    {name:"Mango (per 500g)", price:25, img:"Mango.jpg"},
    {name:"Banana (per 500g)", price:30, img:"Banana.jpg"},
    {name:"Apple (per 500g)", price:45, img:"Apple.jpg"},
    {name:"Orange (per 500g)", price:25, img:"Orange.jpg"},
    {name:"Watermelon (per 500g)", price:40, img:"Watermelon.jpg"},
    {name:"Cherry (per 500g)", price:25, img:"Cherry.jpg"},
    {name:"Papaya (per 500g)", price:25, img:"Papaya.jpg"},
    {name:"Lemon (per 500g)", price:25, img:"Lemon.jpg"},
    {name:"Peach (per 500g)", price:30, img:"peach.jpg"},
];

    const products1kg = [
        {name:"Mango (per kg)", price:50 , img:"Mango.jpg"},
        {name:"Banana (per kg)", price:60, img:"Banana.jpg"},
        {name:"Apple (per kg)", price:90, img:"Apple.jpg"},
        {name:"Orange (per kg)", price:50, img:"Orange.jpg"},
        {name:"Watermelon (per kg)", price:80, img:"Watermelon.jpg"},
        {name:"Cherry (per kg)", price:50, img:"Cherry.jpg"},
        {name:"Papaya (per kg)", price:50, img:"Papaya.jpg"},
        {name:"Lemon (per kg)", price:50, img:"Lemon.jpg"},
        {name:"Peach (per kg)", price:60, img:"peach.jpg"},
    ];

    // --- DOM Elements ---
    const productList = document.getElementById("product-list");
    const cartCountElement = document.getElementById("cart-count");
    
    const homeView = document.getElementById('home-view');
    const checkoutView = document.getElementById('checkout-view');
    
    // Product View Controls
    const view500gLink = document.getElementById("view-500g");
    const view1kgLink = document.getElementById("view-1kg");
    
    // Navigation Controls
    const navHome = document.getElementById('nav-home');
    const navCheckout = document.getElementById('nav-checkout');
    
    // Checkout Elements
    const checkoutForm = document.getElementById("checkout-form");
    const paymentSelect = document.getElementById("paymentMethod");
    const easySection = document.getElementById("easypaisa-section");
    const thankYou = document.getElementById("thankYouMessage");
    const screenshotInput = document.getElementById("screenshot");

    let cartTotal = 0;

    // --- 1. VIEW SWITCHING LOGIC ---
    const setView = (viewId) => {
        homeView.classList.remove('active');
        homeView.classList.add('hidden');
        checkoutView.classList.remove('active');
        checkoutView.classList.add('hidden');
        
        if (viewId === 'home') {
            homeView.classList.add('active');
            homeView.classList.remove('hidden');
        } else if (viewId === 'checkout') {
            checkoutView.classList.add('active');
            checkoutView.classList.remove('hidden');
        }
    };

    navHome.addEventListener('click', (e) => {
        e.preventDefault();
        setView('home');
    });
    
    navCheckout.addEventListener('click', (e) => {
        e.preventDefault();
        setView('checkout');
        // Reset form state when entering checkout
        checkoutForm.reset();
        checkoutForm.style.display = 'block';
        thankYou.style.display = 'none';
        easySection.style.display = 'none';
        document.querySelectorAll(".error").forEach(el => el.style.display = "none");
    });
    
    // --- 2. PRODUCT RENDERING LOGIC ---
    const renderProducts = (productsArray) => {
        productList.innerHTML = ''; 

        productsArray.forEach(p => {
            const card = document.createElement("div");
            card.className = "card";
            card.innerHTML = `
                <img src="${p.img}" alt="${p.name}">
                <div class="card-content">
                    <h3>${p.name}</h3>
                    <p class="price">Price: Rs. ${p.price}</p>
                    <button class="add-btn">Add to Cart</button>
                </div>
            `;
            
            card.querySelector(".add-btn").addEventListener("click", () => {
                cartTotal++;
                cartCountElement.textContent = cartTotal;
            });
            
            productList.appendChild(card);
        });
    };
    
    // Product list switching
    view500gLink.addEventListener('click', (e) => {
        e.preventDefault();
        renderProducts(products500g);
    });

    view1kgLink.addEventListener('click', (e) => {
        e.preventDefault();
        renderProducts(products1kg);
    });

    // --- 3. CHECKOUT FORM LOGIC ---
    
    // Toggle EasyPaisa section visibility and required status
    paymentSelect.addEventListener("change", () => {
        if (paymentSelect.value === "easypaisa") {
            easySection.style.display = "block";
            screenshotInput.setAttribute('required', 'required');
        } else {
            easySection.style.display = "none";
            screenshotInput.removeAttribute('required');
        }
    });

    // Handle Form Submission and Validation
    checkoutForm.addEventListener("submit", (e) => {
        e.preventDefault();

        // Clear previous error messages
        document.querySelectorAll(".error").forEach(el => el.style.display = "none");
        document.querySelectorAll('input, textarea, select').forEach(el => el.classList.remove('invalid'));

        let valid = true;
        
        // Validation function helper
        const validateField = (id, checkFn, errorMsgId) => {
            const input = document.getElementById(id);
            const value = input.value.trim();
            const errorElement = document.getElementById(errorMsgId);
            
            if (!checkFn(value, input)) {
                errorElement.style.display = "block";
                input.classList.add('invalid');
                valid = false;
            } else {
                input.classList.remove('invalid');
            }
        };

        // Validators
        const isRequired = (value) => value.length > 0;
        const isValidEmail = (value) => /\S+@\S+\.\S+/.test(value);
        const isValidPhone = (value) => /^\d{7,}$/.test(value.replace(/\D/g, ''));
        const isPaymentSelected = (value) => value !== "";
        const isScreenshotUploaded = (value, input) => {
            return paymentSelect.value !== "easypaisa" || input.files.length > 0;
        };

        // Run validation checks
        validateField("fullName", isRequired, "error-fullName");
        validateField("email", isValidEmail, "error-email");
        validateField("phone", isValidPhone, "error-phone");
        validateField("address", isRequired, "error-address");
        validateField("paymentMethod", isPaymentSelected, "error-paymentMethod");

        // Specific check for EasyPaisa screenshot
        validateField("screenshot", isScreenshotUploaded, "error-screenshot"); // Assuming you'd add an error div for screenshot if needed

        if (!valid) {
            alert("Please fill out all required fields correctly.");
            return;
        }

        // --- Success Logic ---
        // In a real application, you would send data to a server here.
        setTimeout(() => {
            checkoutForm.style.display = "none";
            thankYou.style.display = "block";
        }, 500);
    });

    // --- Initial setup ---
    renderProducts(products500g); // Load 500g products initially
});