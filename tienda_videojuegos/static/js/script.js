document.addEventListener("DOMContentLoaded", function () {
    const btn = document.getElementById("toggle-theme");
    const html = document.documentElement;
    
    btn.addEventListener("click", function () {
        const current = html.getAttribute("data-bs-theme");
        const newTheme = current === "dark" ? "light" : "dark";
        html.setAttribute("data-bs-theme", newTheme);
        
        // Guardar el estado del tema en localStorage
        localStorage.setItem("theme", newTheme);
    });
    
    // Cargar el estado del tema desde localStorage al cargar la página
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme) {
        html.setAttribute("data-bs-theme", savedTheme);
    }
    
    // Cargar el estado del tema desde localStorage al cambiar de página
    window.addEventListener("beforeunload", function () {
        const currentTheme = html.getAttribute("data-bs-theme");
        localStorage.setItem("theme", currentTheme);
    });
    
    // Cargar el estado del tema desde localStorage al cambiar de vista
    window.addEventListener("hashchange", function () {
        const savedTheme = localStorage.getItem("theme");
        if (savedTheme) {
            html.setAttribute("data-bs-theme", savedTheme);
        }
    });
});