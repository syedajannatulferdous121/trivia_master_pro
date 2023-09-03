import random
import time

# Sample trivia questions and answers organized by categories (you can expand this)
trivia_data = {
    "General Knowledge": [
        {
            "question": "What is the capital of France?",
            "answer": "Paris",
            "hint": "Starts with 'P'",
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "answer": "Mars",
            "hint": "Fourth planet from the Sun",
        },
    ],
    "Animals": [
        {
            "question": "What is the largest mammal in the world?",
            "answer": "Blue Whale",
            "hint": "Lives in the ocean",
        },
    ],
}

# Function to allow users to input a new trivia question
def input_custom_question():
    category = input("Enter the category for your question: ")
    question = input("Enter the question: ")
    answer = input("Enter the answer: ")
    hint = input("Enter a hint (optional): ")

    if category not in trivia_data:
        trivia_data[category] = []

    trivia_data[category].append({
        "question": question,
        "answer": answer,
        "hint": hint,
    })

# Function to start the trivia quiz
def start_trivia():
    score = 0
    high_score = 0
    attempts = 2  # Number of attempts per question
    categories = list(trivia_data.keys())

    while True:
        print("\nWelcome to PyTriviaMasterPro - Test Your Knowledge!")
        print("Choose a category:")

        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")

        category_choice = input("Enter the number of your chosen category (or 'exit' to quit): ")

        if category_choice.lower() == 'exit':
            break
        elif category_choice.lower() == 'add':
            input_custom_question()
            continue

        try:
            category_index = int(category_choice) - 1
            selected_category = categories[category_index]

            questions = trivia_data[selected_category]
            random.shuffle(questions)

            for question_data in questions:
                question = question_data["question"]
                answer = question_data["answer"]
                hint = question_data["hint"]

                print(f"\nCategory: {selected_category}")
                print(f"Question: {question}")

                for attempt in range(attempts):
                    user_answer = input("Your Answer (or 'hint' for a hint): ").strip()

                    if user_answer.lower() == 'hint':
                        print(f"Hint: {hint}")
                        continue

                    if user_answer.lower() == answer.lower():
                        print("Correct!")
                        score += 1
                        break
                    else:
                        print("Wrong answer. Try again.")

                time.sleep(1)  # Pause for a moment before the next question

            print(f"\nQuiz completed! Your score: {score}/{len(questions)}")
            if score > high_score:
                high_score = score
                print(f"New High Score: {high_score}/{len(questions)}")

            play_again = input("Play again? (yes/no): ").lower()
            if play_again != 'yes':
                break

        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid category number.")

if __name__ == "__main__":
    start_trivia()
