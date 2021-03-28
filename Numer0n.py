import random

num1 = random.randint(0, 9)
num2 = random.randint(0, 9)
num3 = random.randint(0, 9)

answer = [num1, num2, num3]

def check_digit(num):
    if num[0] == num[1] or num[1] == num[2] or num[2] == num[0]:
        return True
    else:
        return False

while check_digit(answer):
    num2 = random.randint(0, 9)
    num3 = random.randint(0, 9)
    answer = [num1, num2, num3]



print("Let's start Numer0n!")



def eat_judge(answer, val):
    eat = 0
    for n in range(len(answer)):
        if answer[n] == val[n]:
            eat += 1
    return eat


def bite_judge(answer, val):
    bite = 0
    for n in range(len(answer)):
        for m in range(len(answer)):
            if answer[n] == val[m] and n != m:
                bite += 1
    return bite



n = 1
while n < 11:
    print("Challenge " + str(n))

    val = input('Please enter a 3-digit number : ')

    while True:
        if len(val) != 3:
            val = input('Please enter a 3-digit number again : ')
        elif check_digit(val):
            val = input('Please enter a 3-digit number again : ')
        elif not val[0].isdigit() or not val[1].isdigit() or not val[2].isdigit():
            val = input('Please enter a 3-digit number again : ')
        else:
            break

    val = list(map(int, val))

    
    if answer[0] == val[0] and answer[1] == val[1] and answer[2] == val[2]:
        print("!!---------------------------------!!")
        print("Congratulations!! You won this game!!")
        print("!!---------------------------------!!")
        break
    else:
        if n != 10:
            print("EAT : " + str(eat_judge(answer, val)))
            print("BITE : " + str(bite_judge(answer, val)))
            print("It's wrong.\n")
        else:
            answer = map(str, answer)
            print("You lose this game. The answer is" + ''.join(answer) + ".")

    n += 1
