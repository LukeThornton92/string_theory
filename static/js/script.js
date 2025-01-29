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
