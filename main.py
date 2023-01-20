#import modules
from random import randrange as r
from time import time as t
# ask how many questions user wants
no_question = int(input("How many Question do you want : "))
max_num = int(input("Highest number used in practice? : " ))
#set score start at zero
score = 0
answer_list = []
#loop through number of questions
start = t()
for q in range (no_question):
    num1,num2 = r(1,max_num+1), r(1,max_num+1)
    ans = num1 * num2
    u_ans =  int(input(f"{num1} X {num2} "))
    answer_list.append(f"{num1} X {num2} = {ans}  your ans: {u_ans}")
    if u_ans == ans:
        score += 1
        end = t()
print(f"Thank you for playoing you got {score} out of {no_question} ({round(score/no_question * 100 )}%) correct in {round(end-start,1)} "
      f"second ({round((end-start)/no_question,1)} second/question)")
for a in answer_list:
    print(a)
# create two random numbers and calc answer
# show user the question
# capture answer and modify user score
# output final score
