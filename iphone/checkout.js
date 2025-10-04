document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("checkout-form");
  const paymentSelect = document.getElementById("paymentMethod");
  const easySection = document.getElementById("easypaisa-section");
  const thankYou = document.getElementById("thankYouMessage");

  paymentSelect.addEventListener("change", () => {
    if (paymentSelect.value === "easypaisa") {
      easySection.style.display = "block";
    } else {
      easySection.style.display = "none";
    }
  });

  form.addEventListener("submit", (e) => {
    e.preventDefault();

    document.querySelectorAll(".error").forEach(el => el.style.display = "none");

    let valid = true;

    const fullName = document.getElementById("fullName").value.trim();
    if (!fullName) {
      document.getElementById("error-fullName").style.display = "block";
      valid = false;
    }

    const email = document.getElementById("email").value.trim();
    if (!email || !email.includes("@")) {
      document.getElementById("error-email").style.display = "block";
      valid = false;
    }

    const phone = document.getElementById("phone").value.trim();
    if (!phone) {
      document.getElementById("error-phone").style.display = "block";
      valid = false;
    }

    const address = document.getElementById("address").value.trim();
    if (!address) {
      document.getElementById("error-address").style.display = "block";
      valid = false;
    }

    const paymentMethod = paymentSelect.value;
    if (!paymentMethod) {
      document.getElementById("error-paymentMethod").style.display = "block";
      valid = false;
    }

    if (!valid) return;

    // Simulate order submission
    setTimeout(() => {
      form.style.display = "none";
      thankYou.style.display = "block";
    }, 500);
  });
});