document.addEventListener("DOMContentLoaded", () => {
    const darkModeToggle = document.querySelector("#darkModeToggle");
    const darkModeLabel = document.querySelector('label[for="darkModeToggle"]');

    // Function to set the theme
    const setTheme = (theme) => {
        document.documentElement.setAttribute("data-bs-theme", theme);
        localStorage.setItem("theme", theme);
        if (darkModeToggle) {
            darkModeToggle.checked = theme === "dark";
        }

        if (darkModeLabel) {
            darkModeLabel.textContent = theme === "dark" ? "Dark Mode" : "Light Mode";
        }
    };

    // Check for saved theme in localStorage
    const savedTheme = localStorage.getItem("theme") || "light";
    setTheme(savedTheme);

    // Add event listener for the toggle switch
    if (darkModeToggle) {
        darkModeToggle.addEventListener("change", () => {
            const newTheme = darkModeToggle.checked ? "dark" : "light";
            setTheme(newTheme);
        });
    }
});
