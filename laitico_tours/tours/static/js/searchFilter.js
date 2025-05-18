document.addEventListener("DOMContentLoaded", function () {
    // Get elements
    let searchInput = document.getElementById("search-input");
    let priceFilter = document.getElementById("price-filter");

    // Ensure elements exist before adding event listeners
    if (searchInput && priceFilter) {
        searchInput.addEventListener("keyup", filterDestinations);
        priceFilter.addEventListener("change", filterDestinations);
        filterDestinations(); // Run filter once on page load
    }
});

function filterDestinations() {
    let searchInput = document.getElementById("search-input");
    let priceFilter = document.getElementById("price-filter");

    // Ensure elements exist before proceeding
    if (!searchInput || !priceFilter) return;

    let searchValue = searchInput.value.toLowerCase();
    let priceValue = priceFilter.value;
    let destinations = document.querySelectorAll(".destination");

    destinations.forEach(destination => {
        let nameElement = destination.querySelector("h3");
        let priceElement = destination.querySelector(".price");

        // Ensure elements exist before accessing properties
        if (!nameElement || !priceElement) return;

        let name = nameElement.textContent.toLowerCase();
        let price = parseFloat(priceElement.textContent.replace("Price: $", "").trim());
        let show = true;

        // Apply search filter
        if (!name.includes(searchValue)) {
            show = false;
        }

        // Apply price filter
        if (priceValue === "low" && price >= 500) {
            show = false;
        } else if (priceValue === "medium" && (price < 500 || price > 1000)) {
            show = false;
        } else if (priceValue === "high" && price <= 1000) {
            show = false;
        }

        // Show or hide destination
        destination.style.display = show ? "block" : "none";
    });
}
