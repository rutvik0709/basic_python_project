import getpass
import stdiomask
print("\t\t\t\t########### WELCOME TO QUIZ ###########")

def login(username, password):
    if username == "rutvik" and password == "1234":
        quizgame()
    else:
        print("ERROR!!!!")
        quit()

def quizgame():
    print("----------------------------------------------------------------------------")
    answer1 = input("Question 1 :What is the capital of India?\nAnswer: ").lower()
    answer2 = input("Question 2 :How many state do we have in India?\nAnswer: ").lower()
    answer3 = input("Question 3 :Which cricket player has scored most international centuries?\nAnswer: ").lower()
    answer4 = input("Question 4 :Which is the national flower of India?\nAnswer: ").lower()
    answer5 = input("Question 5 :How many colors are there in a rainbow?\nAnswer: ").lower()
    answer6 = input("Question 6 :Who is the Prime Minister of india?\nAnswer: ").lower()
    answer7 = input("Question 7 :Who is the national animal of India?\nAnswer: ").lower()
    answer8 = input("Question 8 :Who won IPL in 2021?\nAnswer: ").lower()
    answer9 = input("Question 9 :Which is the most electronegative element?\nAnswer: ").lower()
    answer10 = input("Question 10 :Ricky Ponting is also known as what?\nAnswer: ").lower()
    answers =[answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8, answer9, answer10]
    print("----------------------------------------------------------------------------")
    # total_score = score(answers,0)
    # print(total_score)
    grade(score(answers,0))

def score(answers,c):
    correct_answers = ["delhi","twenty nine","sachin","lotus","seven","narendra modi","tiger","chennai super kings","fluorine","punter"]
    for i in range(len(answers)):
        if answers[i] == correct_answers[i]:
            c=c+1
    return c

def grade(total_score):
    if total_score >=8:
        print(f"You scored {total_score}/10. You have A grade.")
    if total_score >=5 and total_score <8:
        print(f"You scored {total_score}/10. You have B grade.")
    if total_score <5:
        print(f"You scored {total_score}/10. You have failed in the quiz.")
    quit()

if __name__=="__main__":
    a = input("USERNAME: ")
    b = stdiomask.getpass("PASSWORD: ")
    login(str(a),str(b))