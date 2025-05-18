document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".faq-question").forEach(question => {
        question.addEventListener("click", () => {
            const faqItem = question.closest(".faq-item");
            const icon = question.querySelector(".toggle-icon");

            if (!faqItem) return;
            
            faqItem.classList.toggle("active");

            icon.textContent = faqItem.classList.contains("active") ? "−" : "+";

            document.querySelectorAll(".faq-item").forEach(item => {
                if (item !== faqItem) {
                    item.classList.remove("active");
                    const otherIcon = item.querySelector(".toggle-icon");
                    if (otherIcon) otherIcon.textContent = "+";
                }
            });
        });
    });
});
