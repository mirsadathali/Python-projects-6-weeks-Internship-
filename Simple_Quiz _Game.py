# Simple Quiz Game
def quiz_game():
    print("Welcome to the Quiz Game!")
    print("Let's test your knowledge.\n")

    # Questions and answers
    questions = [
        {
            "question": "What is the capital of France?",
            "choices": ["1. Paris", "2. Berlin", "3. Madrid", "4. Rome"],
            "answer": 1
        },
        {
            "question": "Which planet is called the Red Planet?",
            "choices": ["1. Earth", "2. Mars", "3. Jupiter", "4. Saturn"],
            "answer": 2
        },
        {
            "question": "What is 5 + 3?",
            "choices": ["1. 5", "2. 8", "3. 10", "4. 15"],
            "answer": 2
        },
        {
            "question": "What is the chemical symbol for water?",
            "choices": ["1.O2", "2.H2O", "3.CO2", "4.H2"],
            "answer": 2
        }
    ]

    score = 0  # To keep track of the user's score

    # Loop through questions
    for i, q in enumerate(questions):
        print(f"Question {i + 1}: {q['question']}")
        for choice in q['choices']:
            print(choice)
        try:
            user_answer = int(input("Enter the number of your answer: "))
            if user_answer == q['answer']:
                print("Correct!\n")
                score += 1
            else:
                print("Wrong! The correct answer was:", q['choices'][q['answer'] - 1], "\n")
        except ValueError:
            print("Invalid input! Moving to the next question.\n")

    # Final Score
    print(f"Quiz Over! Your final score is {score}/{len(questions)}.")

# Start the game
quiz_game()
