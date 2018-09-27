
import random

question_lis = []
answer_lis = []

def set_answer() :
    question = random.randint(1000, 9999)
    question_str = str(question)
    
    question_lis.append(int(question_str[0]))
    question_lis.append(int(question_str[1]))
    question_lis.append(int(question_str[2]))
    question_lis.append(int(question_str[3]))

def couple(e, f) :
    if e == f and question_lis[e] == answer_lis[f] :
        return 'A'
    else :
        return 'B'

def judge_guess(a, b, c, d) :
    answer_lis = [int(a), int(b), int(c), int(d)]
    for i in range(len(question_lis)) :
        print(question_lis[i])
        for j in range(len(answer_lis)) :
            print (answer_lis[j])
            print (question_lis[i], answer_lis[j], end=' ')
            print (type(i), type(j), end = '')
            for k in couple(i, j) :
                print (couple(i, j))   

for k in range (1, 10) :
    set_answer()
    print (question_lis)
    for l in range (1, 10) :
        
        a = input ('a = ')
        b = input ('b = ')
        c = input ('c = ')
        d = input ('d = ')
        judge_guess(a, b, c, d)