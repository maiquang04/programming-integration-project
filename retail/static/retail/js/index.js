document.addEventListener("DOMContentLoaded", function () {
	updateBrowseByCategoryView();
	updateExploreProductsView();
	toggleHoverEffectOnHeart();
});

function updateBrowseByCategoryView() {
	const items = document.querySelectorAll(".category-section__item");
	const prevButton = document.getElementById("section-title-bar__category-prev-button");
	const nextButton = document.getElementById("section-title-bar__category-next-button");
	const itemsPerPage = 6;
	let startIndex = 0;

	function updateView() {
		// Hide all items
		items.forEach((item, index) => {
			item.style.display = index >= startIndex && index < startIndex + itemsPerPage ? "block" : "none";
		});

		// Update button states
		prevButton.disabled = startIndex === 0;
		nextButton.disabled = startIndex + itemsPerPage >= items.length;
	}

	// Event listeners for buttons
	prevButton.addEventListener("click", function () {
		if (startIndex > 0) {
			startIndex -= itemsPerPage;
			updateView();
		}
	});

	nextButton.addEventListener("click", function () {
		if (startIndex + itemsPerPage < items.length) {
			startIndex += itemsPerPage;
			updateView();
		}
	});

	// Initial view update
	updateView();
}

function updateExploreProductsView() {
	const items = document.querySelectorAll("#our-products .product-section__item");
	const prevButton = document.getElementById("section-title-bar__products-prev-button");
	const nextButton = document.getElementById("section-title-bar__products-next-button");
	const itemsPerPage = 8;
	let startIndex = 0;

	function updateView() {
		// Show items within the current range and hide the others
		items.forEach((item, index) => {
			item.style.display = index >= startIndex && index < startIndex + itemsPerPage ? "block" : "none";
		});

		// Enable or disable buttons based on navigation limits
		prevButton.disabled = startIndex === 0;
		nextButton.disabled = startIndex + itemsPerPage >= items.length;
	}

	// Event listeners for navigation buttons
	prevButton.addEventListener("click", function () {
		if (startIndex > 0) {
			startIndex -= itemsPerPage;
			updateView();
		}
	});

	nextButton.addEventListener("click", function () {
		if (startIndex + itemsPerPage < items.length) {
			startIndex += itemsPerPage;
			updateView();
		}
	});

	// Initial rendering of the view
	updateView();
}

function toggleHoverEffectOnHeart() {
	// Select all product thumbnails
	const thumbnails = document.querySelectorAll(".product-section__product-thumbnail");

	thumbnails.forEach((thumbnail) => {
		const heart = thumbnail.querySelector(".product-section__product-heart");

		// Add 'hover' class when mouse enters thumbnail (excluding heart)
		thumbnail.addEventListener("mouseenter", () => {
			thumbnail.classList.add("hover");
		});

		// Remove 'hover' class when mouse leaves thumbnail
		thumbnail.addEventListener("mouseleave", () => {
			thumbnail.classList.remove("hover");
		});

		// Ensure 'hover' class is removed when hovering over the heart
		heart.addEventListener("mouseenter", () => {
			thumbnail.classList.remove("hover");
		});

		// Reapply 'hover' class when leaving the heart
		heart.addEventListener("mouseleave", () => {
			thumbnail.classList.add("hover");
		});
	});
}
