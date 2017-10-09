const admissionNav = document.querySelector('.admission-nav');
const examNav = document.querySelector('.exam-nav');
const personalNav = document.querySelector('.personal-nav');

const adminTable = document.querySelector('#admin-detail');
const examTable = document.querySelector('#qualify-detail');
const addressTable = document.querySelector('#address-detail');

const tables = document.querySelectorAll('table')
const navs = document.querySelectorAll('.leftnav')

function hideAll() {
    tables.forEach(function(table) {
      table.classList.add('hide');
    });
    navs.forEach(function(nav) {
      nav.classList.remove('grey');
    });
}

function displayExamTable() {
  hideAll();
  examTable.classList.remove('hide');
  examNav.classList.add('grey');
}

function displayAddressTable() {
  hideAll();
  addressTable.classList.remove('hide');
  personalNav.classList.add('grey');
}

function displayAdminTable() {
  hideAll();
  adminTable.classList.remove('hide');
  admissionNav.classList.add('grey')
}

admissionNav.addEventListener('click', displayAdminTable);
examNav.addEventListener('click', displayExamTable);
personalNav.addEventListener('click', displayAddressTable);
