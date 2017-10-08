const admissionNav = document.querySelector('.admission-nav');
const examNav = document.querySelector('.exam-nav');
const personalNav = document.querySelector('.personal-nav');

const adminTable = document.querySelector('#admin-detail');
const examTable = document.querySelector('#qualify-detail');
const addressTable = document.querySelector('#address-detail');


function hideAll() {
  examTable.classList.add('hide');
  addressTable.classList.add('hide');
  adminTable.classList.add('hide');
}

function displayExamTable() {
  hideAll();
  examTable.classList.remove('hide');
}

function displayAddressTable() {
  hideAll();
  addressTable.classList.remove('hide');
}

function displayAdminTable() {
  hideAll();
  adminTable.classList.remove('hide');
}

admissionNav.addEventListener('click', displayAdminTable);
examNav.addEventListener('click', displayExamTable);
personalNav.addEventListener('click', displayAddressTable);
