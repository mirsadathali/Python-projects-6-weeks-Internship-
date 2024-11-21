**How to Run**
Clone or Download the repository:

bash
Copy code
git clone https://github.com/your-username/simple-quiz-game.git
cd simple-quiz-game
Ensure Python 3.12 is installed on your system.

Run the script:
bash
Copy code
python quiz_game.py
Follow the on-screen instructions to play the quiz.

**Customization**
Open the quiz_game.py file in any text editor.
Locate the questions list:
python
Copy code


questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["1. Paris", "2. Berlin", "3. Madrid", "4. Rome"],
        "answer": 1
    },
    ...
]


Add or modify questions, choices, and the correct answer (use 1-based indexing for answer).     
Track and save high scores.
