# Quiz by Lyric Marner

score = 0

questions = [
    {
        "question": "1. What organ is responsible for filtering toxins from the blood?",
        "options": ["A. Liver", "B. Pancreas", "C. Kidney", "D. Stomach"],
        "answer": "A"
    },

    {
        "question": "2. What type of blood vessel brings blood towards the heart?",
        "options": ["A. Arteries", "B. Capillaries", "C. Veins", "D. Lymph nodes"],
        "answer": "C"
    },

    {
        "question": "3. How many chambers does the heart have?",
        "options": ["A. 5", "B. 3", "C. 2", "D. 4"],
        "answer": "D"
    }
]

print("=== Welcome to my Anatomy Quiz! ===\n")

for q in questions:
    print(q["question"])

    for option in q["options"]:
        print(option)

    response = input("Enter Your Answer (A, B, C, or D): ").strip().upper()

    if response == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Incorrect... The correct answer was {q['answer']}.\n")

print("=" * 40)
print(f"Your final score is {score}/{len(questions)}")