num_legs = int(input())
num_heads = int(input())

def solve(leg, head):
    num_rabbit = int((leg-2*head)/2)
    num_chicken = int((4*head - leg)/2)
    print("rabbits_num:", num_rabbit)
    print("chicken_num:", num_chicken)

solve(num_legs,num_heads )