class Upper:
    def __init__(self, string):
        self.string = string
    
    def __str__(self):
        b = str(self.string)
        return b.upper()
string1 = str(input())
upp = Upper(string1)
print(upp)

    
