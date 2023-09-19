// AOS
AOS.init({
  once: true, // Set the 'once' option to true to make all animations trigger only once
});


// Swiper
var swiper = new Swiper(".mySwiper", {
  slidesPerView: 4,
  spaceBetween: 30,
  freeMode: true,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
});