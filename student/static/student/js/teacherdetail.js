const profileNav = document.querySelector('.profile-nav');
const coursesNav = document.querySelector('.courses-nav')

const teacherImage = document.querySelector('.teacherimage');
const teacherDetails = document.querySelector('.teacherdetails');
const coursesDetail = document.querySelector('.courses-details');

const navs = document.querySelectorAll('.leftnav');

function hideAll() {
  navs.forEach(function(nav) {
    nav.classList.remove('blue-grey');
  });
  teacherImage.classList.add('hide');
  teacherDetails.classList.add('hide');
  coursesDetail.classList.add('hide');

}

function handleProfileClick() {
  hideAll();
  teacherImage.classList.remove('hide');
  teacherDetails.classList.remove('hide');
  profileNav.classList.add('blue-grey');
}

function handleCoursesClick() {
  hideAll();
  coursesDetail.classList.remove('hide');
  coursesNav.classList.add('blue-grey');
}

profileNav.addEventListener('click', handleProfileClick);
coursesNav.addEventListener('click', handleCoursesClick);
