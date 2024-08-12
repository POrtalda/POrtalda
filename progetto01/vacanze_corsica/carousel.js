document.addEventListener('DOMContentLoaded', function () {
    var myCarousel = document.querySelector('#foto');
    var carousel = new bootstrap.Carousel(myCarousel, {
        interval: 5000, // 5000ms = 5 seconds
        wrap: true
    });
});
