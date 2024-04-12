import random
import time 
from collections import Counter

"needed variables"
check = True
question_file = open("Questions.txt","r") 
questions = []
answer_lenght = []
random_questions = []

"creating questions"

for line in question_file :
    line = line.replace('\n','')
    line = line.split(";")
    questions.append(line)
    
#print(questions)
for i, element in enumerate(questions):
    #print(f"Index {i}: {element}")
    answer_lenght.append(len(element[1])) # number of letter in answer
    
answer_letter_lenght = Counter(answer_lenght) # how many answer have same number of letters

"to sort question's answer from big to small"
myKeys = list(answer_letter_lenght.keys())
myKeys.sort()
sorted_answer_letter_lenght = {i: answer_letter_lenght[i] for i in myKeys}

"creating random question list that includes one question for same letter length"
def Random_Questions_List () : 
    for i in sorted_answer_letter_lenght.keys() : # loop type of answer length 
        #print(i)
        while check : 
            random_question = random.choice(questions)
            if len(random_question[1]) == i :
                random_questions.append(random_question)
                #print(random_question[0])
                questions.remove(random_question)
                break
Random_Questions_List ()
#print(random_questions)

"making * to letter when letter given"
def Change_Letter(secret_word, answer_word, letter):
    new_secret_word = ""
    for i in range(len(answer_word)):
        if answer_word[i] == letter:
            new_secret_word += answer_word[i]
        else:
            new_secret_word += secret_word[i]
    return new_secret_word


"removing all the same letter if one letter located more than one in word"

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]


def Game () : 
    Gamer_Score = 0
    for question in random_questions :
        secret_word = "*" * len(question[1])
        answer_word = question[1]
        answer_word_list = list(answer_word)
        print(question[0], end=" ")
        print(secret_word)
        while "*" in secret_word :
            Gamer_Choice = input("Press 1 to take letter 2 to guess : ")
            if Gamer_Choice == "1" :
                time.sleep(0.5)
                letter = random.choice(answer_word_list)
                
                print(Change_Letter(secret_word, answer_word, letter))
                secret_word = Change_Letter(secret_word, answer_word, letter)
                answer_word_list = remove_values_from_list(answer_word_list,letter)
                #print(answer_word_list)
            elif Gamer_Choice == "2" : 
                Gamer_Guess = input("Please enter your guess : ")
                if Gamer_Guess.lower() == answer_word.lower() :
                    print("Congrats You guessed right. The word is",answer_word)
                    Gamer_Score += secret_word.count("*")*100
                    break
                else :
                    print("You guessed wrong.")
                    break
            else : 
                print("Please Enter Invalid Value")
        "???????????"
        
    print("Your Total Score is :",Gamer_Score)
    
    
"Controlling input and gamestart"    



x="1"

while x == "1": 
    x = input("""HeLLo Welcome to Word Game : 
1 to play word game 2 to exit : """)
    if x == "1" :
        Game()
        x = input("Press 1 to Restart 2 to exit :  ")
    elif x == "2" :
        print("you exitted game")
    else :
        print("Please enter valid value")
        x = "1"
    

