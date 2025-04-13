question = (
    ("What is the capital of France?"),
    ("What is the largest planet in our solar system?"),
    ("What is the smallest prime number?") ,
    ("What is the chemical symbol for gold?"),
    ("What is the largest mammal?"),
           )

options = (("A. Paris", "B. London", "C. Berlin", "D. Madrid"),
           ("A. Jupiter", "B. Earth", "C. Mars", "D. Saturn"),
           ("A. 2", "B. 1", "C. 3", "D. 5"),
           ("A. Au", "B. Ag", "C .Fe", "D. Pb"),
           ("A. Blue Whale", "B. Elephant", "C. Giraffe", "D. Hippopotamus"))

answer = ("A", "A", "A", "A", "A")
guesses = []
score = 0
question_num = 0
for question in question:
    print("------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
        
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)    
    if guess == answer[question_num]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct answer is", answer[question_num])
  
    question_num += 1

print("------------------------")
print("Results")
print("------------------------")
print("Answers: ", end="")
for answer in answer:
    print(answer, end=" ")
print()    

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")

score = int(float(score) / float(len(question)) * 100)  # Ensuring floating-point division
print("Score: ", score, "%")


