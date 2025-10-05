document.addEventListener("DOMContentLoaded", function () {
  const swiper = new Swiper('.gallery-swiper', {
    slidesPerView: 3,
    slidesPerGroup: 1,
    spaceBetween: 20,
    loop: true,
    autoplay: {
      delay: 3000,
      disableOnInteraction: false
    },
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
    breakpoints: {
      768: { slidesPerView: 2 },
      480: { slidesPerView: 1 }
    }
  });
});


// Fotogalerie

//querySelectorAll protože je více img na stránce
const images = document.querySelectorAll('.gallery-img');
const lightbox = document.getElementById('lightbox');
const lightboxImg = document.getElementById('lightbox-img');
const closeBtn = document.getElementById('closeBtn');
const nextBtn = document.getElementById('nextBtn');
const prevBtn = document.getElementById('prevBtn');
const counter = document.getElementById('counter');

let currentIndex = 0;

function showLightbox(index) {
  lightbox.style.display = 'flex';
  lightboxImg.src = images[index].src;
  currentIndex = index;
  counter.textContent = `${index + 1} / ${images.length}`;
}