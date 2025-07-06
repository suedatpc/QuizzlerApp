import requests
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

API_URL = "https://opentdb.com/api.php"

paramaters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(API_URL, params=paramaters)
response.raise_for_status()
data = response.json()
question_data = response.json()["results"]

question_bank = []
for question in question_data:
   question_text = question["question"]
   question_answer = question["correct_answer"]
   new_q = Question(question_text, question_answer)
   question_bank.append(new_q)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
