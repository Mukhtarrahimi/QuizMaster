questions = []
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