document.body.addEventListener("htmx:responseError", function (evt) {
  alert(evt.detail.xhr.responseText);
});

console.log(document.getElementById("myForm"))  

function getnum1() {
  var divElement = document.getElementById("num1");
  var contenuDiv = divElement.textContent;
  return contenuDiv;
}
function getnum2() {
  var divElement = document.getElementById("num2");
  var contenuDiv = divElement.textContent;
  return contenuDiv;
}
function getsigne() {
  var divElement = document.getElementById("signe");
  var contenuDiv = divElement.textContent;
  return contenuDiv;
}
function startCountdown() {
  
  var formDecompte = document.getElementById("formDecompte");
  var inputNumber = document.getElementById("inputNumber");
  var seconds = parseInt(inputNumber.value, 10); // Obtenir la valeur du champ et la convertir en entier
  var countdownElement = document.getElementById("countdown");
  var askElement = document.getElementById("ask"); // Élément div "ask"
  
  // Afficher la div "ask"
  askElement.style.display = "block"; // Ou "inline" ou "inline-block", selon le style souhaité

  // Masquer le champ d'entrée
  formDecompte.style.display = "none";

  var countdownInterval = setInterval(function () {
    if (seconds <= 0) {
      clearInterval(countdownInterval);
      countdownElement.textContent = "Terminé! Redirection...";

      // Effectuer une redirection vers l'URL de la vue Django souhaitée
      window.location.href = "/QuizMath/timeout";
    } else {
      countdownElement.textContent = seconds;
      seconds--;
    }
  }, 1000); // Mettre à jour toutes les 1 seconde (1000 ms)
}

// Masquer la div "ask" lors du chargement de la page
document.addEventListener("DOMContentLoaded", function() {
  var askElement = document.getElementById("ask");
  askElement.style.display = "none";
});