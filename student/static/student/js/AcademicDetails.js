const enrollNav = document.querySelector('.enroll-nav');
const cdNav = document.querySelector('.cd-nav');
const attendanceNav = document.querySelector('.attendance-nav');
const gradeNav = document.querySelector('.grade-nav');

const enrollTable = document.querySelector('#enroll-table');
const cdTable = document.querySelector('#cd-table');
const attendanceTable = document.querySelector('#attendance-table');
const gradeTable = document.querySelector('#grade-table');

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

function displayEnrollTable() {
  hideAll();
  enrollTable.classList.remove('hide');
  enrollNav.classList.add('grey');
}

function displayCdTable() {
  hideAll();
  cdTable.classList.remove('hide');
  cdNav.classList.add('grey');
}

function displayAttendanceTable() {
  hideAll();
  attendanceTable.classList.remove('hide');
  attendanceNav.classList.add('grey');
}

function displayGradeTable() {
  hideAll();
  gradeTable.classList.remove('hide');
  gradeNav.classList.add('grey');
}

enrollNav.addEventListener('click', displayEnrollTable);
cdNav.addEventListener('click', displayCdTable);
attendanceNav.addEventListener('click', displayAttendanceTable);
gradeNav.addEventListener('click', displayGradeTable);
