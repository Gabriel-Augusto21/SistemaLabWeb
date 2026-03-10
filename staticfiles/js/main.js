document.addEventListener("DOMContentLoaded", () => {

    document.getElementById("header").classList.add("show");

    const cards = document.querySelectorAll(".custom-card");
    cards.forEach((card, i) => {
        setTimeout(() => card.classList.add("show"), i * 120);

        card.addEventListener("mouseenter", () => card.classList.add("hovered"));
        card.addEventListener("mouseleave", () => card.classList.remove("hovered"));
        card.addEventListener("mousedown", () => card.classList.add("clicked"));
        card.addEventListener("mouseup", () => card.classList.remove("clicked"));
    });

    document.querySelectorAll(".custom-btn").forEach(btn => {
        btn.addEventListener("click", e => {
            const ripple = document.createElement("span");
            const size = Math.max(btn.clientWidth, btn.clientHeight);
            ripple.style.width = ripple.style.height = size + "px";
            ripple.style.left = e.offsetX - size / 2 + "px";
            ripple.style.top = e.offsetY - size / 2 + "px";
            ripple.classList.add("ripple");
            btn.appendChild(ripple);
            setTimeout(() => ripple.remove(), 600);
        });
    });

});