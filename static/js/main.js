document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("toggle-form");
    const formSection = document.getElementById("add-post");

    toggleButton.addEventListener("click", function () {
        if (formSection.style.display === "none" || formSection.style.display === "") {
            formSection.style.display = "block";
            formSection.classList.add("fade-in");
        } else {
            formSection.style.display = "none";
        }
    });
});
