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
    print("question")
    
   