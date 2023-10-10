import html
import json
import random

from quizApp.models import Quize

def quiz(user):
    # Charger les questions depuis le fichier JSON
    with open('quizApp/quiz.json', 'r', encoding='utf-8') as json_file:
        questions = json.load(json_file)

    # Obtenir la liste des questions déjà posées pour cet utilisateur (à partir de la base de données ou d'un mécanisme de stockage)
    questions_deja_posees = user.questions_repondues.all()  # Vous devez implémenter cela en fonction de votre modèle utilisateur
    liste = [question.Question_id for question in questions_deja_posees]
    # Sélectionner une question aléatoire qui n'a pas encore été posée à cet utilisateur
    available_questions = [key for key in questions.keys() if key not in liste]
    if not available_questions:
        # Toutes les questions ont été posées à cet utilisateur
        return None  # Vous pouvez renvoyer quelque chose pour indiquer que le quiz est terminé

    random_key = random.choice(available_questions)
    random_question = questions[random_key]

    # Décoder les caractères spéciaux dans la question et les réponses
    random_question['question'] = html.unescape(random_question['question'])
    random_question['answers'] = [html.unescape(answer) for answer in random_question['answers']]
    random_question['key'] = random_key
    # Enregistrer la question actuelle comme question posée à l'utilisateur
    #print(user.questions_repondues.set(random_key))  # Vous devez implémenter cela en fonction de votre modèle utilisateur
    user.ajouter_question_repondu(random_key) # Vous devez implémenter cela en fonction de votre modèle utilisateur
    random.shuffle(random_question['answers'])
    return random_question

def getreponce(key):
    with open('quizApp/quiz.json', 'r', encoding='utf-8') as json_file:
        questions = json.load(json_file)
    question = questions[key]

    return question['correct_answer'],question['explanation']

def scorequiz(user,mutiple=5):
    questions_repondues = user.questions_repondues.all()
    false = 0
    for i in questions_repondues:
        if i.user_responce:
            if i.is_true:
                false =false+1
            else:
                false =false-1
    return false*mutiple