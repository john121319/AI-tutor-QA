import learn
import quiz

print('''if you want to learn, enter "learn".
if you want questions, enter "QA".''')
choice = input("learn/QA: ").strip().lower()

if __name__ == "__main__":
    if choice == "learn":
        learn.learn()  # Call the learn function
    elif choice == "qa":
        quiz.quiz()  # Call the quiz function
    else:
        print("Invalid choice! Please enter 'learn' or 'QA'.")