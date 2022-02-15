a = input()
b = [int(i) for i in a.split()]

def prime(element):
    num_devisor = 0
    for i in range(1,element):
        if element %i==0:
            num_devisor+=1
    if(num_devisor==1):
        return element
    else:
        return None

print(list(filter(prime, b)))


