import csv
import random

def load_questions():
    questions = []
    with open("questions.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            questions.append(row)
    return questions

def quiz():
    questions = load_questions()
    # Select 5 random questions
    random_questions = random.sample(questions, 5)  # Randomly selects 5 unique questions
    total_questions = len(random_questions)

    for i in range(total_questions):
        question = random_questions[i]
        print(f"\nQuestion {i + 1} of {total_questions}: {question['question']}")
        print("A.", question["option_a"])
        print("B.", question["option_b"])
        print("C.", question["option_c"])
        print("D.", question["option_d"])

        user_answer = input("Your answer (A, B, C, or D): ").strip().upper()

        if user_answer == question["answer"]:
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {question['answer']}: {question['explanation']}")