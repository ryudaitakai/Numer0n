import random


numlist = list(range(10))

num1 = numlist.pop(random.randint(0, len(numlist) - 1))
num2 = numlist.pop(random.randint(0, len(numlist) - 1))
num3 = numlist.pop(random.randint(0, len(numlist) - 1))

answer = [num1, num2, num3]



def check_digit(num):
    return len(num) != len(set(num))


def eat_judge(answer, num_3dig):
    eat = 0
    for n in range(len(answer)):
        if answer[n] == num_3dig[n]:
            eat += 1
    return eat


def bite_judge(answer, num_3dig):
    bite = 0
    for n in range(len(answer)):
        for m in range(len(answer)):
            if answer[n] == num_3dig[m] and n != m:
                bite += 1
    return bite



print("Let's start Numer0n!")

n = 1
while n < 11:
    print("Challenge " + str(n))

    num_3dig = input('Please enter a 3-digit number : ')

    while True:
        if len(num_3dig) != 3:
            num_3dig = input('Please enter a 3-digit number again : ')
        elif check_digit(num_3dig):
            num_3dig = input('Please enter a 3-digit number again : ')
        elif not num_3dig[0].isdigit() or not num_3dig[1].isdigit() or not num_3dig[2].isdigit():
            num_3dig = input('Please enter a 3-digit number again : ')
        else:
            break

    num_3dig = list(map(int, num_3dig))

    
    if answer[0] == num_3dig[0] and answer[1] == num_3dig[1] and answer[2] == num_3dig[2]:
        print("!!---------------------------------!!")
        print("Congratulations!! You won this game!!")
        print("!!---------------------------------!!")
        break
    else:
        if n != 10:
            print("EAT : " + str(eat_judge(answer, num_3dig)))
            print("BITE : " + str(bite_judge(answer, num_3dig)))
            print("It's wrong.\n")
        else:
            answer = map(str, answer)
            print("You lose this game. The answer is " + ''.join(answer) + ".")

    n += 1
