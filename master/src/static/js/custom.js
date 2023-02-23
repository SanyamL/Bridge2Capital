$(window).scroll(function () {
    var scroll = $(window).scrollTop();

    if (scroll >= 50) {
        $("header").addClass("fixed");
    } else {
        $("header").removeClass("fixed");
    }
});


$('.work-carousel .owl-carousel').owlCarousel({
    center: true,
    URLhashListener: true,
    autoplayHoverPause: true,
    startPosition: 'URLHash',
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 1,
            margin: 20,
            loop: true,
            //            margin: 0,
        },
        1000: {
            items: 1,
            margin: 50,
            loop: true,
            //            margin: 0,
        },
        1200: {
            items: 2,
            margin: 150,
            loop: false,
            //            stagePadding: 200,
        },
        1500: {
            items: 2,
            margin: 250,
            loop: false,
            //                        stagePadding: 400,
        }
    }
});

// Go to the next item
$('.leftarrow').click(function (e) {
    $('.work-carousel .owl-carousel').trigger("prev.owl");
})
// Go to the previous item
$('.rightarrow').click(function (e) {
    $('.work-carousel .owl-carousel').trigger("next.owl");
})


$('.payment-carousel .owl-carousel').owlCarousel({
    loop: true,
    margin: 10,
    autoplay: true,
    nav: true,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 1
        },
        1000: {
            items: 1
        }
    }
});

// Go to the next item
$('.leftarrow').click(function (e) {
    $('.payment-carousel .owl-carousel').trigger("prev.owl");
})
// Go to the previous item
$('.rightarrow').click(function (e) {
    $('.payment-carousel .owl-carousel').trigger("next.owl");
})









$('.customer-carousel .owl-carousel').owlCarousel({
    loop: true,
    margin: 10,
    nav: true,
    autoplay: true,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 1
        },
        1000: {
            items: 1
        }
    }
});

// Go to the next item
$('.leftarrow').click(function (e) {
    $('.customer-carousel .owl-carousel').trigger("prev.owl");
})
// Go to the previous item
$('.rightarrow').click(function (e) {
    $('.customer-carousel .owl-carousel').trigger("next.owl");
})









$('.youtube-carousel .owl-carousel').owlCarousel({
    loop: true,
    margin: 10,
    nav: true,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 1
        },
        1000: {
            items: 1
        }
    }
});

// Go to the next item
$('.leftarrow').click(function (e) {
    $('.youtube-carousel .owl-carousel').trigger("prev.owl");
})
// Go to the previous item
$('.rightarrow').click(function (e) {
    $('.youtube-carousel .owl-carousel').trigger("next.owl");
})





$('.brand-carousel-1 .owl-carousel').owlCarousel({
    loop: false,
    autoplay: false,
    nav: true,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 4
        },
        1000: {
            items: 4,
            margin: 60,
            stagePadding: 100,
        }
    }
});


$('.brand-carousel .owl-carousel').owlCarousel({
    loop: true,
    autoplay: true,
    nav: true,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 4
        },
        1000: {
            items: 4,
            margin: 60,
            stagePadding: 100,
        }
    }
});




$('.testimonial-carousel .owl-carousel').owlCarousel({
    loop: false,
    center: true,
    URLhashListener: true,
    autoplayHoverPause: true,
    startPosition: 'URLHash',
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 2,
            margin: 20,
        },
        1000: {
            items: 2,
            margin: 40,
        },
        1500: {
            items: 2,
            margin: 80,
        }
    }
});









$(function () {
    $('a[href*="#"]:not([href="#"])').click(function () {
        if(!$(this).hasClass('banner-grp')){
            if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
                var target = $(this.hash);
                target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
                if (target.length) {
                    $('html, body').animate({
                        scrollTop: target.offset().top
                    }, 1000);
                    return false;
                }
            }
        }
    });
});

$(function () {
    var Accordion = function (el, multiple) {
        this.el = el || {};
        this.multiple = multiple || false;

        // Variables privadas
        var links = this.el.find('.card-header');
        // Evento
        links.on('click', {
            el: this.el,
            multiple: this.multiple
        }, this.dropdown)
    }

    Accordion.prototype.dropdown = function (e) {
        var $el = e.data.el;
        $this = $(this),
            $next = $this.next();

        $next.slideToggle();
        $this.parent().toggleClass('open');

        if (!e.data.multiple) {
            $el.find('.card-body').not($next).slideUp().parent().removeClass('open');
        };
    }

    var accordion = new Accordion($('#accordion'), false);
});

$(function () {
    var Accordion = function (el, multiple) {
        this.el = el || {};
        this.multiple = multiple || false;

        // Variables privadas
        var links = this.el.find('.card-header');
        // Evento
        links.on('click', {
            el: this.el,
            multiple: this.multiple
        }, this.dropdown)
    }

    Accordion.prototype.dropdown = function (e) {
        var $el = e.data.el;
        $this = $(this),
            $next = $this.next();

        $next.slideToggle();
        $this.parent().toggleClass('open');

        if (!e.data.multiple) {
            $el.find('.card-body').not($next).slideUp().parent().removeClass('open');
        };
    }

    var accordion = new Accordion($('#accordion1'), false);
});
// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
  }