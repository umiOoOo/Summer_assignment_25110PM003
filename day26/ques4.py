# Q104: Write a program to Create quiz application.

# Define questions, options, and answers
questions = [
    {
        "question": "What is the correct file extension for Python files?",
        "options": ["A) .pt", "B) .py", "C) .pyt", "=D) .pyw"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["A) function", "B) fun", "C) def", "D) define"],
        "answer": "C"
    }
]

score = 0

print("--- Welcome to the Python Quiz! ---\n")

# Loop through quiz items
for i, q in enumerate(questions):
    print(f"Question {i + 1}: {q['question']}")
    for option in q['options']:
        print(option)
        
    user_answer = input("Your answer (A/B/C/D): ").upper()
    
    if user_answer == q['answer']:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer was {q['answer']}.\n")

print(f"Quiz Complete! Your total score is {score}/{len(questions)}")