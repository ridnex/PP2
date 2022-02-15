# to be honest I din't have any idea to solve this problem 
# so i used google and understand main idea 
# in that case it is not my idea, but at least i wrote it by myself

word= str(input())

def permut(string :str):
    if len(string) ==  1:
        return [string]
    else:
        part = permut(string[1:])
        element = string[0]
        answer = []
        for i in part:
            for j in range(len(i)+1):
                answer.append(i[:j]+element+i[j:])
        return answer

print(permut(word))

