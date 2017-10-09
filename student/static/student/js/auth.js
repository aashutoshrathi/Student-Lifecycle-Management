const [user, pass] = ['test', 'test'];
const [tuser, tpass] = ['teach', 'teach'];
const loginBtn = document.querySelector('.loginbtn');


function auth() {
  const username = document.querySelector('.username').value;
  const password = document.querySelector('.secret').value;
  console.log(username, password);
  if (username == user && password == pass)
    window.location = "StudentProfile.html";

  else if (username == tuser && password == tpass)
      window.location = "TeacherProfile.html";

}

loginBtn.addEventListener('click', auth);
