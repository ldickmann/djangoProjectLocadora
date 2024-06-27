// Muda cor da navbar ao rolar a página
window.addEventListener('scroll', () => {
  const navbar = document.getElementById('mainNav');
  if (window.pageYOffset > 100) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
});