const enrollNav = document.querySelector('.enroll-nav');
const cdNav = document.querySelector('.cd-nav');
const attendanceNav = document.querySelector('.attendance-nav');
const gradeNav = document.querySelector('.grade-nav');

const enrollTable = document.querySelector('#enroll-table');
const cdTable = document.querySelector('#cd-table');
const attendanceTable = document.querySelector('#attendance-table');
const gradeTable = document.querySelector('#grade-table');

const tables = document.querySelectorAll('table')

function hideAll() {
    tables.forEach(function(table) {
      table.classList.add('hide');
    });
}

function displayEnrollTable() {
  hideAll();
  enrollTable.classList.remove('hide');
}

function displayCdTable() {
  hideAll();
  cdTable.classList.remove('hide');
}

function displayAttendanceTable() {
  hideAll();
  attendanceTable.classList.remove('hide');
}

function displayGradeTable() {
  hideAll();
  gradeTable.classList.remove('hide');
}

enrollNav.addEventListener('click', displayEnrollTable);
cdNav.addEventListener('click', displayCdTable);
attendanceNav.addEventListener('click', displayAttendanceTable);
gradeNav.addEventListener('click', displayGradeTable);
