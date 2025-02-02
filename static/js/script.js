//Search bar in header added functionality.
document.addEventListener("DOMContentLoaded", function () {
  const searchInput = document.getElementById("searchright");
  const searchButton = document.querySelector(".searchbutton");
  let isExpanded = false;

  searchButton.addEventListener("click", function (event) {
    event.preventDefault();

    if (!isExpanded) {
      // First click: Expand the search bar
      searchInput.style.width = "363px";
      searchInput.focus();
      isExpanded = true;
    } else {
      // Second click: If there's text, submit the form; if not, close the bar
      if (searchInput.value.trim() !== "") {
        searchInput.closest("form").submit();
      } else {
        searchInput.style.width = "0px";
        searchInput.blur(); // Remove focus
        isExpanded = false;
      }
    }
  });
});

// Function to adjust the number of recommended products based on screen size
function adjustRecommendedProducts() {
  const products = document.querySelectorAll(".product-card"); // Select all product cards
  const windowWidth = window.innerWidth; // Get the current window width

  // Calculate the number of products to display based on screen size
  let numToShow = 1; // Default for mobile
  if (windowWidth >= 576 && windowWidth < 992) {
    numToShow = 2; // Show 2 products on small screens (tablet)
  } else if (windowWidth >= 992 && windowWidth < 1200) {
    numToShow = 3; // Show 3 products on medium screens
  } else if (windowWidth >= 1200) {
    numToShow = 4; // Show 4 products on large screens
  }

  // Loop through all products and hide or show based on the calculated numToShow
  products.forEach((product, index) => {
    if (index >= numToShow) {
      product.style.display = "none"; // Hide products that exceed the number to display
    } else {
      product.style.display = "block"; // Show products within the limit
    }
  });
}

// Run the function when the page is loaded and whenever the window is resized
window.addEventListener("DOMContentLoaded", adjustRecommendedProducts);
window.addEventListener("resize", adjustRecommendedProducts);
