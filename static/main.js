const swiper = new Swiper('.netflix-carousel', {
  slidesPerView: 5.5,
  spaceBetween: 16,
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  grabCursor: true,
  rewind: true, // volta ao início quando chega no fim
});