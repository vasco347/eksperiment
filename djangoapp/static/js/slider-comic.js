$(document).ready(function(){
      $('.slider-comic').slick({
        slidesToShow: 4,
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