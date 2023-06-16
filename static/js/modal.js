// Получаем ссылки на элементы
var modal = document.getElementById("registrationModal");
var loginModal = document.getElementById("loginModal");
var btn = document.getElementById("openModalLogin");
var btn_login = document.getElementById("openloginModal");
var btn_registration = document.getElementById("registrationModalOpen");
var closeBtn = document.getElementsByClassName("close")[0];

// При нажатии на кнопку "Открыть модальное окно" отображаем модальное окно
btn.onclick = function() {
  modal.style.display = "block";
}

btn_login.onclick = function() {
    loginModal.style.display = "block";
    modal.style.display = "none";
}

btn_registration.onclick = function() {
    modal.style.display = "block";
    loginModal.style.display = "none";
}

// При нажатии на "крестик" закрываем модальное окно
closeBtn.onclick = function() {
  modal.style.display = "none";
  loginModal.style.display = "none";
}



// При клике вне модального окна закрываем его
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }

  if (event.target == loginModal) {
    loginModal.style.display = "none";
}
}