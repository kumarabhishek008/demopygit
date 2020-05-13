class divide:

    def __init__(self,num1,num2):
        self.num1 =num1
        self.num2=num2

    def __divmod__(self):


        c = self.num1/self.num2


        return c
num1 = float(input("enter value 1-"))
num2 = float(input("enter value 2-"))

result1 = divide(num1,num2)
result = result1.__divmod__()
print(result)