
let openShopping = document.querySelector(".shopping");
let closeShopping = document.querySelector(".closeShopping");
let list = document.querySelector(".list");
let listCard = document.querySelector(".listCard");
let body = document.querySelector("body");
let total = document.querySelector(".total");
let quantity = document.querySelector(".quantity");

openShopping.addEventListener("click", () => {
  // Check if the cart is empty
  if (quantity.innerText === "0") {
    // Redirect to another page
    window.location.href = "{% url 'empty' %}";
  } else {
    // If the cart is not empty, add 'active' class to the body
    body.classList.add("active");
  }
  // body.classList.add('active');
});
closeShopping.addEventListener("click", () => {
  body.classList.remove("active");
});

let products = [
  {
    id: 1,
    name: "Veg Burger",
    image: "{% static 'images/blog-1.jpg' %}",
    price: 80,
  },
  {
    id: 2,
    name: "Mayo Burger",
    image: "{% static 'images/blog-2.jpg' %}",
    price: 100,
  },
  {
    id: 3,
    name: "Mango juice",
    image: "{% static 'images/4.PNG' %}",
    price: 100,
  },
  {
    id: 4,
    name: "Fried Rice",
    image: "{% static 'images/img1.jpg' %}",
    price: 100,
  },
  {
    id: 5,
    name: "Salad",
    image:"{% static 'images/5.PNG' %}",
    price: 150,
  },
  {
    id: 6,
    name: "Pizza",
    image: "{% static 'images/6.PNG' %}",
    price: 120,
  },
];
let listCards = [];
function initApp() {
  products.forEach((value, key) => {
    let newDiv = document.createElement("div");
    newDiv.classList.add("item");
    newDiv.innerHTML = `
            <img src="images/${value.image}"/>
            <div class="title">${value.name}</div>
            <div class="price">${value.price.toLocaleString()}</div>
            <button onclick="addToCard(${key})">Add To Card</button>`;
    list.appendChild(newDiv);
  });
}
initApp();
function addToCard(key) {
  if (listCards[key] == null) {
    // copy product form list to list card
    listCards[key] = JSON.parse(JSON.stringify(products[key]));
    listCards[key].quantity = 1;
  }
  reloadCard();
}
function reloadCard() {
  listCard.innerHTML = "";
  let count = 0;
  let totalPrice = 0;
  var itemsForCheckout = []; // Array to store items for checkout

  listCards.forEach((value, key) => {
    totalPrice = totalPrice + value.price;
    count = count + value.quantity;
    if (value != null) {
      let newDiv = document.createElement("li");
      newDiv.innerHTML = `
                <div><img src="images/${value.image}"/></div>
                <div>${value.name}</div>
                <div>${value.price.toLocaleString()}</div>
                <div>
                    <button onclick="changeQuantity(${key}, ${
        value.quantity - 1
      })">-</button>
                    <div class="count">${value.quantity}</div>
                    <button onclick="changeQuantity(${key}, ${
        value.quantity + 1
      })">+</button>
                </div>`;
      listCard.appendChild(newDiv);
      itemsForCheckout.push({
        name: value.name,
        price: value.price,
        quantity: value.quantity,
        
      });
    }
  });

  total.innerText = "Total Price: " + totalPrice;

  localStorage.setItem("price", JSON.stringify(totalPrice));
  quantity.innerText = count;
  localStorage.setItem("itemsForCheckout", JSON.stringify(itemsForCheckout));
  // window.location.href = 'payment.html';
}

function changeQuantity(key, quantity) {
  if (quantity == 0) {
    delete listCards[key];
  } else {
    listCards[key].quantity = quantity;
    listCards[key].price = quantity * products[key].price;
  }
  reloadCard();
}

document.getElementById("total_amt").addEventListener("click", function () {
  // Redirect user to the next page
  window.location.href = "payment.html";
});
