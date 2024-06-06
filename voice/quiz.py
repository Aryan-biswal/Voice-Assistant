quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Lisbon"],
        "answer": "Paris"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["Harper Lee", "Mark Twain", "J.K. Rowling", "Ernest Hemingway"],
        "answer": "Harper Lee"
    }
]

def start_quiz():
    score = 0
    for q in quiz_questions:
        print(q["question"])
        for i, option in enumerate(q["options"], start=1):
            print(f"{i}. {option}")
        answer = input("Choose the correct option number: ")
        if q["options"][int(answer) - 1] == q["answer"]:
            score += 1
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer is {q['answer']}.\n")
    return f"Your final score is {score} out of {len(quiz_questions)}."
