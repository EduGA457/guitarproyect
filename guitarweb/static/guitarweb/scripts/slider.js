document.addEventListener('DOMContentLoaded', function() {
    // Selecciona todas las imágenes del slider
    let slides = document.querySelectorAll('.slider-image');
    let currentSlide = 0;

    // Funcion que cambia el slide
    function changeSlides() {
        // Verifica que haya slides
        if (slides.length === 0) {
            console.error("No hay imágenes en el slider");
            return;
        }

        slides[currentSlide].classList.remove('active'); 

        currentSlide = (currentSlide + 1) % slides.length; 

        slides[currentSlide].classList.add('active'); 
    }

    // Verifica que haya al menos una imagen antes de iniciar el intervalo
    if (slides.length > 0) {
        // cambia el slider cada 3 seg
        setInterval(changeSlides, 3000);
    } else {
        console.error("No se encontraron imágenes en el slider");
    }
});