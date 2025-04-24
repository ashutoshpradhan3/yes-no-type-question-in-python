import random

# List of questions with correct answers (True/False)
question_bank = [
    ("Is Python a programming language?", True),
    ("Is HTML a programming language?", False),
    ("Does the Earth have two moons?", False),
    ("Is 2 a prime number?", True),
    ("Can elephants fly naturally?", False),
    ("Is Java platform-independent?", True),
    ("Is CSS used for designing layout and styles?", True),
    ("Is 100 greater than 200?", False),
    ("Does water boil at 100°C at sea level?", True),
    ("Is '==' used for assignment in Python?", False)
]

# Randomly select 5 questions
selected_questions = random.sample(question_bank, 5)

score = 0

print("Answer the following questions with 'yes' or 'no':\n")

for i, (question, correct_answer) in enumerate(selected_questions, start=1):
    user_input = input(f"Q{i}: {question} ").strip().lower()

    # Convert user input to Boolean
    if user_input in ['yes', 'y']:
        user_answer = True
    elif user_input in ['no', 'n']:
        user_answer = False
    else:
        print("Invalid input! Skipping this question.\n")
        continue

    # Compare with correct answer
    if user_answer == correct_answer:
        score += 1
        print("Correct!\n")
    else:
        print("Incorrect.\n")

print(f"Your final score is: {score}/5")
