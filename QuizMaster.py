import json
with open("python_questions.json", "r", encoding="utf-8") as f:
    questions = json.load(f)
print(f"Loaded {len(questions)} questions.")


def add_question():
    print("Add a new question")
    question_text = input("Enter your question: ")
    options = []
    for op in range(4):
        op_text = input(f"Option {op + 1}: ")
        options.append(op_text)
    correct = int(input("Correct answer (1-4): "))

    new_id = questions[-1]['id'] + 1 if questions else 1
    questions.append({
        "id": new_id,
        "question": question_text,
        "options": options,
        "answer": correct
    })
    print("Question added successfully.")


def start_quiz():
    print("Welcome to the quiz!")
    if not questions:
        print("No questions available. Please add some questions first.")
        return
    score = 0
    for i, q in enumerate(questions):
        print(f"Question {i+1}: {q['question']}")
        for idx, opt in enumerate(q['options']):
            print(f"{idx + 1}. {opt}")
        try:
            answer = int(input("Enter your answer: ")) - 1
            if answer == q['answer'] - 1:
                score += 1
                print("Correct answer!\n")
            else:
                print(f"Incorrect answer. The correct answer was {q['answer']}.\n")
        except:
            print("Invalid input!\n")
   
    show_result(score, len(questions))
                

def show_result(score, total):
    avg = (score / total) * 100
    print("result of quiz!")
    print(f"Your score is {score} out of {total} > {round(avg, 2)}%")
    if avg > 90:
        print("Great!")
    elif avg > 70:
        print("Good!")
    else:
        print("need to more try!")

def view_all_question():
    if not questions:
        print("no questions available.\n")
        return

    print("All Registered Questions:\n")
    for i, q in enumerate(questions):
        print(f"question {i+1}: {q['question']}")
        for idx, opt in enumerate(q['options']):
            print(f"   {idx + 1}. {opt}")
        print(f"Correct Answer: {q['answer']}\n")


def delete_question():
    if not questions:
        print(" No questions to delete.\n")
        return

    print("\nDelete a Question")
    for i, q in enumerate(questions):
        print(f"{i + 1}. {q['question']}")

    try:
        choice = int(input("Enter the number of the question to delete: "))
        if 1 <= choice <= len(questions):
            removed = questions.pop(choice - 1)
            print(f"Deleted: {removed['question']}\n")
        else:
            print("Invalid number. No question deleted.\n")
    except ValueError:
        print("nvalid input. Please enter a number.\n")
        
def save_question():
    if not questions:
        print("No questions to save.\n")
        return

    with open("python_questions.json", "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)

    print("All questions saved to python_questions.json\n")


        
def load_question():
    global questions
    try:
        with open("python_questions.json", "r", encoding="utf-8") as f:
            questions = json.load(f)
        print("Questions loaded from python_questions.json\n")
    except FileNotFoundError:
        print("python_questions.json not found.\n")

         
def menu():
    print("QuizMaster - Quiz System")
    print(".1 Add new question")
    print(".2 Start quiz")
    print(".3 View all questions")
    print(".4 delete question")
    print(".5 Save Questions to File")
    print(".6 Load Questions from File")
    print(".7 Exit")
    
menu()

while True:
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
        menu()
        