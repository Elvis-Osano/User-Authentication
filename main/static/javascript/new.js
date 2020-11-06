const password = document.getElementById("id_password");
const message = document.querySelector(".message");

document.addEventListener("DOMContentLoaded", (e) => {
  if (password) {
    password.remove();
  }
  if (message) {
    setTimeout(() => {
      message.remove();
    }, 5000);
  }
});
