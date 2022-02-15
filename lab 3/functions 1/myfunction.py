#1.py
def convert_g(gram):
    ounces =float( 28.3495231 * gram)
    return ounces
#2.py
def convert_gradus(F):
    C=(float(F)-32)*(5/9)
    return C
#3.py
def solve(leg, head):
    num_rabbit = int((leg-2*head)/2)
    num_chicken = int((4*head - leg)/2)
    print("rabbits_num:", num_rabbit)
    print("chicken_num:", num_chicken)

#4.py
def prime(element):
    num_devisor = 0
    for i in range(1,element):
        if element %i==0:
            num_devisor+=1
    if(num_devisor==1):
        return element
    else:
        return None

#6.py
def reverse_arr_of_str(arr):
    for i in range(len(arr)//2):
        k = arr[i]
        arr[i]=arr[len(arr)-1-i]
        arr[len(arr)-1-i]=k

    return arr

#7.py
def has_33(arr):
    d = 0 
    for i in range(len(arr)-1):
        if(arr[i]==3 and arr[i+1]==3):
            d+=1
            return True
    if d==0:
        return False
    
#8.py

def has_007(arr: list):
    c= ""
    for i in range(len(arr)):
        if arr[i]==7 or arr[i]==0:
            c = str(c) + str(arr[i])

    if "007" in c:
        return True
    else:
        return False

#10.py
def uniq(arr: list):
    new_arr= []
    for i in arr:
        if i not in new_arr:
            new_arr.append(i)
    return new_arr

#11.py

def polindrom(a: str):
    s = str("")
    for i in range(len(a)-1,-1 ,-1):
        s=str(s)+str(a[i])
    if s==a:
        return True
    else:
        return False

#12.py
def histogram(x):
    s = str("")
    for i in range(x):
        s=s+"*"
    return(s)

#13.py
def random_find(b, atempt, random_num, name):
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
