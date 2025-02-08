document.getElementById("fb").addEventListener("click", function() {
    // Redirect user to the next page
    window.location.href = "login2.html"; // Replace "next_page.html" with your actual next page URL
  });


  document.getElementById("phone_no").addEventListener("click", function() {
    // Redirect user to the next page
    window.location.href = "login3.html"; // Replace "next_page.html" with your actual next page URL
  });

  function validateForm() {
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var emailError = document.getElementById("emailError");
    var passwordError = document.getElementById("passwordError");
    var isValid = true;

    // Reset error messages
    emailError.innerHTML = "";
    passwordError.innerHTML = "";

    // Validate email
    if (!email) {
        emailError.innerHTML = "Email is required";
        isValid = false;
    } else if (!isValidEmail(email)) {
        emailError.innerHTML = "Invalid email format";
        isValid = false;
    }

    // Validate password
    if (!password) {
        passwordError.innerHTML = "Password is required";
        isValid = false;
    }
    // Check if both email and password are empty
    if (!email && !password) {
        emailError.innerHTML = "Email is required";
        passwordError.innerHTML = "Password is required";
        isValid = false;
    }

    return isValid;
}

function isValidEmail(email) {
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}



  

