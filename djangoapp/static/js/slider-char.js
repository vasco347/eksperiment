$(document).ready(function(){
$('.slider-char').slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    arrows: false,
    dots: false,
    speed: 300,
    variableWidth: true,
    infinite: false,
    responsive: [
  {
    breakpoint: 991,
    settings: {
      slidesToShow: 1,
    }
  },
  {
    breakpoint: 767,
    settings: {
      centerMode: true,
      slidesToShow: 1,
    }
  }
]
  });
});