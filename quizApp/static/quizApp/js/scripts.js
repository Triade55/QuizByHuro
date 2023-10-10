const API_URL = 'https://opentdb.com/api.php?amount=10&category=19'; // Par exemple, récupérer 10 questions
const API_KEY = 'YOUR_API_KEY'; // Remplacez par votre clé API

fetch(`${API_URL}`)
  .then(response => response.json())
  .then(data => {
    // Traitez les données du quiz ici
    console.log(data);
  })
  .catch(error => console.error('Erreur lors de la récupération des questions du quiz', error));
