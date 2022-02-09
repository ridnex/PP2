a = input()
a1 = [str(i) for i in a.split("+") ]
def convert(b):
    c = []
    d=""
    for i in range(len(b)):
        
        d = str(d) + str(b[i])
        if(i%3==2):
            d1 = d.replace("ONE",'1')
            d2 = d1.replace("TWO",'2')
            d3 = d2.replace("THR",'3')
            d4 = d3.replace("FOU",'4')
            d5 = d4.replace("FIV",'5')
            d6 = d5.replace("SIX",'6')
            d7 = d6.replace("SEV",'7')
            d8 = d7.replace("EIG",'8')
            d9 = d8.replace("NIN",'9')
            d10 = d9.replace("ZER",'0')
            c.append(d10)
            d=""
    return(c)
cnt=0
for i in a1:
    num=""
    for j in (convert(i)):
        num=str(num)+j
    cnt=+cnt+int(num)

anw = str(cnt)

d1 = anw.replace("1", "ONE")
d2 = d1.replace('2', "TWO")
d3 = d2.replace('3', "THR")
d4 = d3.replace('4', "FOU")
d5 = d4.replace('5', "FIV")
d6 = d5.replace('6', "SIX")
d7 = d6.replace('7', "SEV")
d8 = d7.replace('8', "EIG")
d9 = d8.replace('9', "NIN")
d10 = d9.replace('0',"ZER")
print(str(d10))





    