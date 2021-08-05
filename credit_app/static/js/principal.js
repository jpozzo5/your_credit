const divlogin = document.getElementById('login');
const btnregister = document.getElementById('registro_boton')
const btnstudend = document.getElementById('btn_show_form_studend')
const divRegister = document.getElementById('register')
const divSelection = document.getElementById('selection')

btnregister.onclick = function () {
    divlogin.style.display = "none"
    divSelection.style.display = "block"

};

btnstudend.onclick = function () {
    divRegister.style.display = "block"
    divSelection.style.display = "none"

};