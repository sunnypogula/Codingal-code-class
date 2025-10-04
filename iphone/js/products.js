const products = [
  { name: "Mango (per kg)", price: 50, img: "Mango.jpg" },
  { name: "Banana (per kg)", price: 60, img: "Banana.avif" },
  { name: "Apple (per kg)", price: 90, img: "Apple.jpg" },
  { name: "Orange (per kg)", price: 50, img: "Orange.jpg" },
  { name: "Watermelon (per kg)", price: 80, img: "Watermelon.jpg" },
  { name: "Cherry (per kg)", price: 50, img: "Cherry.jpg" },
  { name: "Papaya (per kg)", price: 50, img: "Papaya.jpg" },
  { name: "Lemon (per kg)", price: 50, img: "Lemon.jpg" },
  { name: "Peach (per kg)", price: 60, img: "peach.jpg" },
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