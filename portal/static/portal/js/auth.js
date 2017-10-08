const [user, pass] = ['test', 'test'];
const [tuser, tpass] = ['teach', 'teach'];
const loginBtn = document.querySelector('.loginbtn');


function auth() {
  const username = document.querySelector('.username').value;
  const password = document.querySelector('.secret').value;
  console.log(username, password);
  if (username == user && password == pass)
    window.location = "portal/student/profile/201651031";

  else if (username == tuser && password == tpass)
      window.location = "ndr001.html";

}

loginBtn.addEventListener('click', auth);
