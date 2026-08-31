/*
    Student Name: Kayla Wagner
    File Name: script.js
    Date: 9 Aug 2023
*/

//Hamburger menu function
function hamburger() {
    var menu = document.getElementById("menu-links");
    var logo = document.getElementById("shred-logo");

    if (menu.style.display === "block" && logo.style.display === "none") {
        menu.style.display = "none";
        logo.style.display = "block";
    } else {
        menu.style.display = "block";
        logo.style.display = "none";
    }
}

function hide() {
    var text = document.querySelector(".hero-img")

    if (text.style.display === "none") {
        text.style.display = "block";
    } else {
        text.style.display = "none";
    }
}


var swiper = new Swiper(".slide-content", {
        slidesPerView: 3,
        spaceBetween: 25,
        loop: true,
        centerSlide: 'true',
        fade: 'true',
        grabCursor: 'true',
        pagination: {
          el: ".swiper-pagination",
          clickable: true,
          dynamicBullets: true,
        },
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev",
        },

        breakpoints:{
            0: {
                slidesPerView: 1,
            },
            640: {
                slidesPerView: 2,
            },
            1015: {
                slidesPerView: 3,
            },
        },
   });