document.addEventListener("DOMContentLoaded", function () {
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
});
