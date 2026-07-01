document.addEventListener("DOMContentLoaded", function () {
    const btn = document.getElementById("toggle-theme");
    const html = document.documentElement;
    
    btn.addEventListener("click", function () {
        const current = html.getAttribute("data-bs-theme");
        const newTheme = current === "dark" ? "light" : "dark";
        html.setAttribute("data-bs-theme", newTheme);
    });
});

