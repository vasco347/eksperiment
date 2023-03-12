$(document).ready(function(){
    $('.slider-movie').slick({
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
        slidesToShow: 3,
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