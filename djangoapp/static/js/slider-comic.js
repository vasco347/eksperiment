$(document).ready(function(){
      $('.slider-comic').slick({
        slidesToShow: 6,
        slidesToScroll: 1,
        arrows: false,
        dots: false,
        speed: 300,
        variableWidth: true,
        infinite: false,
        responsive: [
          {
            breakpoint: 1024,
            settings: {
              slidesToShow: 3,
              slidesToScroll: 1,
              arrows: false,
              dots: false,
              speed: 300,
              variableWidth: true,
              infinite: false,
            }
          },
          {
            breakpoint: 960,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 1,
              arrows: false,
              dots: false,
              speed: 300,
              variableWidth: true,
              infinite: false,
            }
          },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 1,
          arrows: false,
          dots: false,
          speed: 300,
          variableWidth: true,
          infinite: false,
        }
      }
    ]
      });
    });