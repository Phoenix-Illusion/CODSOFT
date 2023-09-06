import random

# Define quiz questions and answers
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "What is the largest mammal on Earth?",
        "options": ["Giraffe", "Hippopotamus", "Elephant", "Blue Whale"],
        "answer": "Blue Whale"
    },
    {
        "question": "What is the powerhouse of the cell?",
        "options": ["Nucleus", "Cell Wall", "Chloroplast", "Mitochondrion"],
        "answer": "Mitochondrion"
    }
]

def run_quiz():
    score = 0
    
    # Display welcome message and rules
    print("Welcome to the Quiz Game!")
    print("You will be asked a series of questions. Choose the correct answer from the options.")
    print("Let's begin!\n")
    
    # Shuffle the quiz questions to make it more engaging
    random.shuffle(quiz_questions)
    
    # Iterate through questions
    for idx, question_data in enumerate(quiz_questions, 1):
        print(f"Question {idx}: {question_data['question']}")
        for i, option in enumerate(question_data['options'], 1):
            print(f"{i}. {option}")
        
        user_answer = input("Your answer (enter the number): ")
        correct_answer = question_data['answer']
        
        if user_answer.isdigit() and 1 <= int(user_answer) <= len(question_data['options']):
            user_answer = question_data['options'][int(user_answer) - 1]
        
        # Evaluate the user's answer
        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}\n")
    
    # Calculate and display the final score
    print(f"Your final score is: {score}/{len(quiz_questions)}")
    
    # Provide feedback based on the score
    if score == len(quiz_questions):
        print("Congratulations! You got a perfect score.")
    elif score >= len(quiz_questions) / 2:
        print("Well done! You did a good job.")
    else:
        print("Keep practicing. You can do better!")
    
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        run_quiz()
    else:
        print("Thank you for playing!")

# Run the quiz game
run_quiz()
