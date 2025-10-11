// app.js

document.addEventListener('DOMContentLoaded', () => {
    
    // --- Product Data Consolidation ---
    const products500g = [
        {name:"Mango (per 500g)", price:25, img:"Mango.jpg", unit: '500g'},
        {name:"Banana (per 500g)", price:30, img:"Banana.avif", unit: '500g'},
        {name:"Apple (per 500g)", price:45, img:"Apple.jpg", unit: '500g'},
        {name:"Orange (per 500g)", price:25, img:"Orange.jpg", unit: '500g'},
        {name:"Watermelon (per 500g)", price:40, img:"Watermelon.jpg", unit: '500g'},
        {name:"Cherry (per 500g)", price:25, img:"Cherry.jpg", unit: '500g'},
        {name:"Papaya (per 500g)", price:25, img:"Papaya.jpg", unit: '500g'},
        {name:"Lemon (per 500g)", price:25, img:"Lemon.jpg", unit: '500g'},
        {name:"Peach (per 500g)", price:30, img:"peach.jpg", unit: '500g'},
    ];

    const products1kg = [
        {name:"Mango (per kg)", price:50 , img:"Mango.jpg", unit: '1kg'},
        {name:"Banana (per kg)", price:60, img:"Banana.avif", unit: '1kg'},
        {name:"Apple (per kg)", price:90, img:"Apple.jpg", unit: '1kg'},
        {name:"Orange (per kg)", price:50, img:"Orange.jpg", unit: '1kg'},
        {name:"Watermelon (per kg)", price:80, img:"Watermelon.jpg", unit: '1kg'},
        {name:"Cherry (per kg)", price:50, img:"Cherry.jpg", unit: '1kg'},
        {name:"Papaya (per kg)", price:50, img:"Papaya.jpg", unit: '1kg'},
        {name:"Lemon (per kg)", price:50, img:"Lemon.jpg", unit: '1kg'},
        {name:"Peach (per kg)", price:60, img:"peach.jpg", unit: '1kg'},
    ];

    // --- DOM Elements ---
    const productList = document.getElementById("product-list");
    const cartCountElement = document.getElementById("cart-count");
    const view500gLink = document.getElementById("view-500g");
    const view1kgLink = document.getElementById("view-1kg");
    
    // Initialize cart total (this should ideally use LocalStorage for persistence)
    let cartTotal = 0;

    // --- Core Rendering Function ---
    const renderProducts = (productsArray) => {
        // Clear existing products
        productList.innerHTML = ''; 

        productsArray.forEach(p => {
            const card = document.createElement("div");
            card.className = "card";
            card.innerHTML = `
                <img src="${p.img}" alt="${p.name}">
                <div class="card-content">
                    <h3>${p.name}</h3>
                    <p class="price">Price: Rs. ${p.price}</p>
                    <button class="add-btn" data-product-unit="${p.unit}">Add to Cart</button>
                </div>
            `;
            
            // Add event listener to the "Add to Cart" button
            card.querySelector(".add-btn").addEventListener("click", () => {
                cartTotal++;
                cartCountElement.textContent = cartTotal;
                console.log(`Added ${p.name} to cart. Total items: ${cartTotal}`);
            });
            
            productList.appendChild(card);
        });
    };

    // --- Navigation Switching Logic ---
    view500gLink.addEventListener('click', (e) => {
        e.preventDefault();
        renderProducts(products500g);
    });

    view1kgLink.addEventListener('click', (e) => {
        e.preventDefault();
        renderProducts(products1kg);
    });

    // --- Initial Load ---
    // Render the 500g list by default when the page loads
    renderProducts(products500g);
});