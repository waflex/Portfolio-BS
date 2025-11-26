document.addEventListener("DOMContentLoaded", () => {
  const glitchElements = document.querySelectorAll(".glitch");

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("glitch-active");
        } else {
          entry.target.classList.remove("glitch-active");
        }
      });
    },
    { threshold: 0.2 }
  );

  glitchElements.forEach((el) => observer.observe(el));
});
