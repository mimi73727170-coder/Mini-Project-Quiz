print("MINI PROECT : Python Quiz")
score = 0
answer = input("What is Python ?")
answer = answer.lower()
if "programming" in answer and "language" in answer :
    print("Correct!")
    score += 1
else :
    print("Wrong!")
print("score :",score)



correct_answer = [
    "Print() is used to show information on the screen.",
    "Print() display texts or values.",
    "Print() print output on the console."
]
answer = input("What does print() do ? ").lower()
if answer in correct_answer :
    print("Correct!")
    score += 1
else :
    print("Wrong!")
print("score :",score)



answer = input("What symbol is used for comments ?")
if answer == "#" :
    print("Correct !")
    score += 1
else :
    print("Wrong!")
print("score :",score)



answer = input("Which keyword create a function?").lower()
if answer == "def" :
    print("Correct!")
    score += 1
else :
    print("Wrong!")
print("score :",score)


answer = input("Which data type stores text ?").lower()
if answer == "str" :
    print("Correct!")
    score += 1
else :
    print("Wrong!")
print("score :",score)

print("SCORE :",score," /5")

if score == 5 :
    print("Excellent!")
elif score >= 3 :
    print("Good Job!")
else :
    print("Keep Practicing!")
    





