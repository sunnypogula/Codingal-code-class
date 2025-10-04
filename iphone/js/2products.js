const products = [
  { name: "Mango (per g)", price: 25, img: "Mango.jpg" },
  { name: "Banana (per g)", price: 30, img: "Banana.avif" },
  { name: "Apple (per g)", price: 45, img: "Apple.jpg" },
  { name: "Orange (per g)", price: 45, img: "Orange.jpg" },
  { name: "Watermelon (per g)", price: 40, img: "Watermelon.jpg" },
  { name: "Cherry (per g)", price: 25, img: "Cherry.jpg" },
  { name: "Papaya (per g)", price: 25, img: "Papaya.jpg" },
  { name: "Lemon (per g)", price: 25, img: "Lemon.jpg" },
  { name: "Peach (per g)", price: 30, img: "peach.jpg" },
];

const productList = document.getElementById("product-list");
const cartCount = document.getElementById("cart-count");
let cartTotal = 0;

products.forEach(product => {
  const card = document.createElement("div");
  card.className = "card";
  card.innerHTML = `
    <img src="${product.img}" alt="${product.name}">
    <div class="card-content">
      <h3>${product.name}</h3>
      <p class="price">Price: Rs. ${product.price}</p>
      <button class="add-btn">Add to Cart</button>
    </div>
  `;
  card.querySelector(".add-btn").addEventListener("click", () => {
    cartTotal++;
    cartCount.textContent = cartTotal;
  });
  productList.appendChild(card);
});