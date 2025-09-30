const swiper = new Swiper('.swiper', {
    slidesPerView: 3,       // kolik obrázků vedle sebe
    slidesPerGroup: 1,      // o kolik se má posunout
    spaceBetween: 20,       // mezera mezi obrázky
    loop: true,             // zapneme "nekonečný" posuv

    autoplay: {
        delay: 3000,          // čas v ms (3 sekundy)
        disableOnInteraction: false // autoplay pokračuje i po kliknutí
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
        768: {slidesPerView: 2},
        480: {slidesPerView: 1}
    }
});
