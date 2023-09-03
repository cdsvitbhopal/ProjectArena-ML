document.addEventListener("DOMContentLoaded", function() {
    const submitBtn = document.getElementById("Submit");
    const myLink = document.getElementById("Submit");
  
    // Add a click event listener to the custom submit button
    submitBtn.addEventListener("click", function() {
      // Get the form element by its ID
      const myForm = document.getElementById("form");
  
      // Manually trigger form validation using checkValidity()
      if (myForm.checkValidity()) {
        // If the form is valid, submit it
        myForm.submit();
      } else {
        // If the form is not valid, display an error message or take appropriate action
        alert("Please fill in all required fields.");
      }
    });
  
    // Add a click event listener to the link
    myLink.addEventListener("click", function(event) {
      // Prevent the default link behavior (preventing it from navigating to "#")
      event.preventDefault();
  
      // Check if the form is valid before navigating to the next page
      const myForm = document.getElementById("form");
      if (myForm.checkValidity()) {
        // If the form is valid, navigate to the desired URL
        window.location.href = "file:///C:/Users/HP/Documents/Data%20Science%20Project/Movie%20recommendation%20system/Thank%20You.html";
      } else {
        // If the form is not valid, display an error message or take appropriate action
        alert("Please fill in all required fields.");
      }
    });
  });
  
    