def quiz_program():
    questions = {
        "What is the capital of France?": "Paris",
        "Who wrote 'Romeo and Juliet'?": "Shakespeare",
        "What is 2 + 2?": "4"
    }
    
    score = 0
    for question, answer in questions.items():
        user_answer = input(f"{question} ").strip()
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {answer}.")
    
    print(f"You got {score}/{len(questions)} questions right!")

quiz_program()
