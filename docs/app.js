const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('#navigation');
if (toggle && nav) {
  toggle.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') !== 'true';
    toggle.setAttribute('aria-expanded', String(open));
    nav.classList.toggle('open', open);
  });
  nav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
    toggle.setAttribute('aria-expanded', 'false'); nav.classList.remove('open');
  }));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && nav.classList.contains('open')) {
      toggle.setAttribute('aria-expanded', 'false'); nav.classList.remove('open'); toggle.focus();
    }
  });
}
const privacyDialog = document.querySelector('#privacy-dialog');
if (privacyDialog) {
  document.querySelectorAll('[data-privacy-open]').forEach(button => button.addEventListener('click', () => privacyDialog.showModal()));
  document.querySelectorAll('[data-privacy-close]').forEach(button => button.addEventListener('click', () => privacyDialog.close()));
}
