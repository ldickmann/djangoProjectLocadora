// Muda cor da navbar ao rolar a página
window.addEventListener('scroll', () => {
  const navbar = document.getElementById('mainNav');
  if (window.pageYOffset > 100) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
});

// Adiciona efeito ao passar o mouse, apresenta um texto.
const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
});

// Abre e fecha o menu navbar no mobile
document.addEventListener('click', () => {
  const navbarToggler = document.querySelector('.navbar-toggler');
  const navbarCollapse = document.querySelector('#navbarNav');

  navbarToggler.addEventListener('click', () => {
    setTimeout(() => {
      if (navbarCollapse.classList.contains('show')) {
        navbarCollapse.classList.remove('show');
        navbarCollapse.style.display = 'none';
      } else {
        navbarCollapse.classList.add('show');
        navbarCollapse.style.display = 'block';
      }
    }, 10);
  });
});