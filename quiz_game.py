def new_game():

    guesses = []
    correct_guess = 0
    question_num = 1

    for key in questions:
        print("--------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter(A, B, C, D ): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guess += check_ans(questions.get(key), guess)
        question_num += 1
    display_score(correct_guess,guesses)
#--------------------------
def check_ans(answer , guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("Wrong")
        return 0

#--------------------------
def display_score(correct_guess,guesses):
    print("--------------------------")
    print("RESULTS")
    print("--------------------------")
    print("Answers: ",end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()


    print("guesses: ",end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int(correct_guess/len(questions)*100)
    print("Your score is "+ str(score)+"%")

#--------------------------
def play_again():
    resp = input("Do you wanna play again? (Yes/No)")
    resp = resp.upper()
    if resp == "YES":
        return True
    else:
        return False
    #--------------------------

questions = {
    "who created python? ": "A",
    "What year was python is created? ": "B",
    "Pyton is tributed to which comedy group? ": "C",
    "Is the earth round? ": "A"
}
options= [
    ["A. Guido Van Rossum", "B. Elon Musk", "C. Dr. APJ abdul kalam","D. Narendra Modi"],
    ["A. 2002","B. 1991","C. 2001", "D. 1994"],
    ["A. Lonely Island","B. Smoosh","C. Monty Python","D. Virgin maria Beach"],
    ["A. True", "B. Absoulutely Not", "C. No it's flat","D. No"]
]
new_game()

while play_again():
    new_game()

print("Byeeee!!")

