
class add:

    def __init__(self,num1,num2):
        self.num1 =num1
        self.num2=num2

    def __add__(self):


        c = self.num1+self.num2


        return c
num1 = float(input("enter value 1-"))
num2 = float(input("enter value 2-"))

result1 = add(num1,num2)
result = result1.__add__()
print(result)