function navigateToRight() {
    let slides = document.querySelectorAll('.slide');
    let activeSlideIndex = Number(0);

    // find index of active slide
    for (const slide of slides) {
        if (slide.classList.contains('active')) {
            // if we're at the end of the slides
            activeSlideIndex = Number(slide.dataset.index);
            if (activeSlideIndex === slides.length - 1) {
                slide.classList.remove('active');
                document.getElementById('slide-0').classList.add('active');
                document.getElementById('slide-0').scrollIntoView();
                break;
            } else {
                slide.classList.remove('active');
                activeSlideIndex = Number(slide.dataset.index) + 1;

                let nextSlide = document.getElementById('slide-' + activeSlideIndex);

                nextSlide.classList.add('active')
                nextSlide.scrollIntoView({ behavior: "smooth", block: "end" });
                break;
            }
        }
    }
}

function animationEndListener(event) {
    console.error('event', event);
    event.target.classList.remove('active');
    // event.target.classList.remove('scroll');
    // event.target.classList.add('hidden');
}

function scrollRight() {
    let slides = document.querySelectorAll('.slide');
    let activeSlideIndex = Number(0);

    let slideToScroll;
    for (const slide of slides) {
        if (slide.classList.contains('active')) {
            // if we're at the end of the slides
            if (activeSlideIndex === slides.length - 1) {
                slideToScroll = slides.item(0)
            } else {
                // slide.addEventListener('animationend', animationEndListener, false);
                activeSlideIndex = Number(slide.dataset.index) - 1;
                slide.scrollIntoView();
                return;
                // slides.item(activeSlideIndex).classList.add('scroll-right');
            }

        }
    }
}

function navigateToLeft() {
    let slides = document.querySelectorAll('.slide');
    let activeSlideIndex = Number(0);

    // find index of active slide
    for (const slide of slides) {
        if (slide.classList.contains('active')) {
            // if we're at the end of the slides
            if (activeSlideIndex === slides.length - 1) {
                console.log('INDEX AND LENGTH MATCH');
                slides.item(0).classList.add('active');
                slides.item(0).classList.remove('hidden');
            } else {
                slide.addEventListener('animationend', animationEndListener, false);
                activeSlideIndex = Number(slide.dataset.index) - 1;
                slides.item(activeSlideIndex).classList.add('scroll-right');
            }

        }
    }

    console.log('ACTIVE SLIDE INDEX ============> ', activeSlideIndex);
    slides.item(activeSlideIndex).classList.add('active');
}
