document.body.addEventListener("htmx:responseError", function (evt) {
  alert(evt.detail.xhr.responseText);
});

function startCountdown() {
  
  var inputNumber = document.getElementById("inputNumber");
  var seconds = parseInt(inputNumber.value, 10); // Obtenir la valeur du champ et la convertir en entier
  var countdownElement = document.getElementById("countdown");

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

function getquestion() {
  var divElement = document.getElementById("question_div");
  var contenuDiv = divElement.textContent;
  return contenuDiv;
}