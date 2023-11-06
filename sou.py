import random
import numpy as np

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3,4,5,6,7,8,9]:
                return level
        except ValueError:
            continue

def generate_number(n):
    while True:
        try:
            guess_0 = []
            guess_1 = ""
            if n == 1:
                x = np.random.randint(0, 9)
            else:
                x = np.random.randint(10**(n-1), 10**(n)-1)
            for i in str(x): #x =1234
                guess_0.append(i) #guess_0 = [1,2,3,4]
            if len(set(guess_0)) == len(guess_0):
                for i in guess_0:
                    guess_1 += i + ''
                break
            else:
                raise ValueError
        except ValueError:
            continue
    return guess_1

def guess_number(n):
    while True:
        try:
            ans_0 = int(input("Guess the number: "))
            ans_1 = []
            for i in str(ans_0):
                ans_1.append(i)
            if len(ans_1) != n:
                raise ValueError
            elif len(set(ans_1)) == len(ans_1):
                break
            else:
                raise ValueError
        except ValueError:
            print("Please import the right form of number")
            continue
    return ans_0

ans_list = [] #list so MAY CHO
guess_list = [] #list so MINH DOAN

l = get_level()
number = generate_number(l) #1234
for m in str(number):
    ans_list.append(m) #[1,2,3,4]

print(number)

counter = 0
while counter != 3:
    one = 0 # trung so
    double = 0 #trung so va vi tri
    play = guess_number(l)
    for n in str(play):
        guess_list.append(n) #tao list chua ky tu ma minh doan
    if ans_list == guess_list:
        print("You're win!")
        break
    else:
        for i in guess_list:
            if i in ans_list and ans_list.index(i) != guess_list.index(i):
                one += 1
            elif i in ans_list and ans_list.index(i) == guess_list.index(i):
                double += 1
        print("Please try again!", "\n", one, "one, ", double, "double")
        counter += 1
        continue

if counter == 3:
    print(f"Sorry, the answer is {number}")