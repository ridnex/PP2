b = [int(i) for i in input().split()]

def prime(element):
    num_devisor = 0
    for i in range(1,element):
        if element %i==0:
            num_devisor+=1
    if(num_devisor==1):
        return True
    
    
Primes =list(filter(lambda x: prime(x), b))
print(Primes)