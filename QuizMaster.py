questions = [
    {
        "question": "What is the correct file extension for Python files?",
        "options": [".pt", ".py", ".pyt", ".python"],
        "answer": 2  # .py
    },
    {
        "question": "Which data type is used to store text in Python?",
        "options": ["int", "str", "bool", "float"],
        "answer": 2  # str
    },
    {
        "question": "How do you start a function in Python?",
        "options": ["function myFunc():", "def myFunc():", "func myFunc():", "start myFunc():"],
        "answer": 2  # def myFunc():
    },
    {
        "question": "Which keyword is used for a conditional statement in Python?",
        "options": ["if", "for", "loop", "define"],
        "answer": 1  # if
    },
    {
        "question": "What will be the output of: print(type(3.5))?",
        "options": ["<class 'int'>", "<class 'float'>", "<class 'str'>", "<class 'bool'>"],
        "answer": 2  # float
    }
]

def add_question():
    print("Add a new question")
    question_text = input("Enter your question: ")
    options = []
    for op in range(4):
        op = input(f"option {op +1}:")
        options.append(op)
    correct = int(input("correct answer(1-4): ")) 
    questions.append({
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