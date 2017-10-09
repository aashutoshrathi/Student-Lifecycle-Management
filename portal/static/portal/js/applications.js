const withdrawForm = document.querySelector('.withdraw-form');
const certificateForm = document.querySelector('.certificates');

const withdrawNav = document.querySelector('.withdraw-nav');
const certificateNav = document.querySelector('.certificate-nav');

const navs = document.querySelectorAll('.leftnav');

function hideAll() {
  withdrawForm.classList.add('hide');
  certificateForm.classList.add('hide');
  navs.forEach(function(nav) {
    nav.classList.remove('grey');
  })
}

function handleWithdrawForm() {
  hideAll();
  withdrawForm.classList.remove('hide');
  withdrawNav.classList.add('grey');
}

function handleCertificateForm() {
  hideAll();
  certificateForm.classList.remove('hide');
  certificateNav.classList.add('grey');
}

withdrawNav.addEventListener('click', handleWithdrawForm);
certificateNav.addEventListener('click', handleCertificateForm);
