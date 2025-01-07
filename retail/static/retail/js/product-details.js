const quantityInput = document.getElementById('quantity_input');
function increment(){
    const currentValue = parseInt(quantityInput.value,10) || 1;
    quantityInput.value = currentValue +1;
}
function decrement(){
    const currentValue = parseInt(quantityInput.value,10) || 1;
    quantityInput.value = currentValue -1;
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
