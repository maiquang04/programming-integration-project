const quantityInput = document.getElementById('quantity_input');
function increment(){
    const currentValue = parseInt(quantityInput.value,10) || 1;
    quantityInput.value = currentValue +1;
}
function decrement(){
    const currentValue = parseInt(quantityInput.value,10) || 1;
    quantityInput.value = currentValue -1;
}
function toggleWishlist(icon_wrapper) {
    const icon = icon_wrapper.querySelector('.wishlist_icon');
    // Toggle the 'selected' class
    icon.classList.toggle('selected');

    // Toggle the class for the icon
    icon.classList.toggle('fa-regular');
    icon.classList.toggle('fa-solid');

    // Optionally, perform some action (e.g., save/remove from the backend)
    if (icon.classList.contains('selected')) {
        console.log("Added to wishlist");
        // Make a call to your backend to add this item to the wishlist
    } else {
        console.log("Removed from wishlist");
        // Make a call to your backend to remove this item from the wishlist
    }
}
const primaryImage = document.getElementById('primary-image');

function changeImage(clickedImage) {
    if(clickedImage != primaryImage){
    primaryImage.src= clickedImage.src;
    primaryImage.animate(
        [
          { opacity: 0 }, // Starting state
          { opacity: 1 }  // Ending state
        ],
        {
          duration: 2000, // 1 second duration
          easing: 'ease' // Animation easing
        }
      );
    }
}
const modal_img= document.getElementById("modal-img");
const modal = document.querySelector('.modal');
primaryImage.onclick = function(){
    
    modal.style.display = "block";
    modal_img.src= primaryImage.src;
}
const close_btn= document.querySelector('.close-btn');
close_btn.onclick = ()=>{
    modal.style.display='none';
}
