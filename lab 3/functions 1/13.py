import random
random_num = random.randint(1, 20)
print("Hello! What is your name?")
name = input()
print("Well, "+name+", I am thinking of a number between 1 and 20.")
print("Take a guess.")
num_from_name = int(input())
atempt = 1
def random_find(b, atempt):
    if int(b)<random_num:
        print("Your guess is too low.")
        print("Take a guess.")
        return False
    elif int(b)>random_num:
        print("Your guess is too more.")
        print("Take a guess.")
        return False
    else:
        print("Good job, "+name+"! You guessed my number in "+str(atempt)+" guesses!")
        return True

while(random_find(num_from_name, atempt)!=True):
    num_from_name = int(input())
    atempt +=1

