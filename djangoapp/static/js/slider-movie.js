$(document).ready(function(){
  $('.slider-movie').slick({
    slidesToShow: 2,
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
      slidesToShow: 1,
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