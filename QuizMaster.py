import json

#  JSON
def load_question():
    global questions
    try:
        with open("python_questions.json", "r", encoding="utf-8") as f:
            questions = json.load(f)
        print(f"Loaded {len(questions)} questions from python_questions.json\n")
    except FileNotFoundError:
        questions = []
        print("python_questions.json not found. Starting with empty question list.\n")

# Question save to JSON file
def save_question():
    if not questions:
        print("No questions to save.\n")
        return
    with open("python_questions.json", "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    print("All questions saved to python_questions.json\n")

def add_question():
    print("Add a new question")
    question_text = input("Enter your question: ")
    options = []
    for i in range(4):
        op_text = input(f"Option {i + 1}: ")
        options.append(op_text)
    while True:
        try:
            correct = int(input("Correct answer (1-4): "))
            if 1 <= correct <= 4:
                break
            else:
                print("Answer must be between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")
    new_id = questions[-1]['id'] + 1 if questions else 1
    questions.append({
        "id": new_id,
        "question": question_text,
        "options": options,
        "answer": correct
    })
    print("Question added successfully.\n")

def start_quiz():
    if not questions:
        print("No questions available. Please add some questions first.\n")
        return
    print("Welcome to the quiz!")
    score = 0
    for i, q in enumerate(questions):
        print(f"\nQuestion {i+1}: {q['question']}")
        for idx, opt in enumerate(q['options']):
            print(f"  {idx + 1}. {opt}")
        while True:
            try:
                answer = int(input("Enter your answer (1-4): "))
                if 1 <= answer <= 4:
                    break
                else:
                    print("Answer must be between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")
        if answer == q['answer']:
            score += 1
            print("Correct answer!")
        else:
            correct_opt = q['options'][q['answer'] - 1]
            print(f"Incorrect answer. Correct answer is: {q['answer']}. {correct_opt}")
    show_result(score, len(questions))

def show_result(score, total):
    percent = (score / total) * 100
    print("\nQuiz Result:")
    print(f"Your score: {score} / {total} ({percent:.2f}%)")
    if percent >= 90:
        print("Excellent! ")
    elif percent >= 70:
        print("Good job! ")
    else:
        print("Keep practicing! ")

def view_all_question():
    if not questions:
        print("No questions available.\n")
        return
    print("\nAll Registered Questions:\n")
    for i, q in enumerate(questions):
        print(f"{i+1}. {q['question']}")
        for idx, opt in enumerate(q['options']):
            print(f"   {idx+1}. {opt}")
        print(f"Correct answer: {q['answer']}\n")

def delete_question():
    if not questions:
        print("No questions to delete.\n")
        return
    print("\nDelete a Question")
    for i, q in enumerate(questions):
        print(f"{i+1}. {q['question']}")
    try:
        choice = int(input("Enter question number to delete: "))
        if 1 <= choice <= len(questions):
            removed = questions.pop(choice - 1)
            print(f"Deleted question: {removed['question']}\n")
        else:
            print("Invalid question number.\n")
    except ValueError:
        print("Invalid input! Please enter a number.\n")

def menu():
    print("\nQuizMaster - Quiz System")
    print("1. Add new question")
    print("2. Start quiz")
    print("3. View all questions")
    print("4. Delete question")
    print("5. Save questions to file")
    print("6. Load questions from file")
    print("7. Exit")

# --- Main program ---

questions = []
load_question()

while True:
    menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        add_question()
    elif choice == "2":
        start_quiz()
    elif choice == "3":
        view_all_question()
    elif choice == "4":
        delete_question()
    elif choice == "5":
        save_question()
    elif choice == "6":
        load_question()
    elif choice == "7":
        print("Exiting QuizMaster. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
