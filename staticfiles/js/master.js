document.addEventListener("DOMContentLoaded", () => {
    window.addEventListener("scroll", () => {
        const nav = document.querySelector(".navbar");
        if (window.scrollY > 10) nav.classList.add("scrolled");
        else nav.classList.remove("scrolled");
    });
});