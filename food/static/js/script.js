let navbar = document.querySelector('.navbar')

document.querySelector('#menu-btn').onclick = () =>{
    navbar.classList.toggle('active');
    // loginForm.classList.remove('active');
    searchForm.classList.remove('active');
}

let searchForm = document.querySelector('.search-form')

document.querySelector('#search-btn').onclick = () =>{
    searchForm.classList.toggle('active');
    navbar.classList.remove('active');
    // loginForm.classList.remove('active');
}

window.onscroll = () =>{
    navbar.classList.remove('active');
    // loginForm.classList.remove('active');
    searchForm.classList.remove('active');
}
 
var swiper = new Swiper(".review-slider", {
    loop:true,
    spaceBetween: 30,
    centeredSlides: true,
    autoplay: {
        delay: 5500,
        disableOnInteraction: false,
    },
    pagination: {
        el: ".swiper-pagination",
    },
});


// document.getElementById("cart-btn").addEventListener("click", function() {
//     // Redirect user to the next page
//     window.location.href = "{% url 'cart' %}"; // Replace 'cart' with the name of your cart view URL pattern
//   });   



// document.getElementById('payButton').addEventListener('click', function (event) {
//     event.preventDefault(); // Prevent form submission

//     // Get form values
//     var n1 = document.getElementById('rname').value;
//     var d1 = document.getElementById('date').value;
//     var t1 = document.getElementById('time').value;
//     var p1 = document.getElementById('people').value;
    

//     // Store data in local storage
//     localStorage.setItem("rname",n1);
//     localStorage.setItem('date', d1);
//     localStorage.setItem('time', t1);
//     localStorage.setItem("people",p1);
    
//   });
//   function redirectToBookingPage2() {
//     // Validate form fields
//     var mobileNo = document.getElementById("rname").value;
//     var date = document.getElementById("date").value;
//     var time = document.getElementById("time").value;
//     var people = document.getElementById("people").value;

//     // Check if all fields are filled
//     if (mobileNo === "" && date === "" && time === "" && people === "" ) {
//         alert("Please fill in all details.");
//         return false; // Prevent form submission
//     }
//     if (mobileNo.length !== 10) {
//         alert("Mobile number should be 10 digits long.");
//         return false; // Prevent form submission
//     }
//      // Check if people is within the range of 1 to 10
//      if (people < 1 || people > 30) {
//         alert("Number of people should be between 1 and 30.");
//         return false; // Prevent form submission
//     }

//     // window.location.href = "{% url 'book1' %}";
//     return true; // Allow form submission
   
// }
