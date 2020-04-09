class Calculator:
    num=100
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def getData(self):
        print("Method in Class")

    def Summation(self):
        return self.num1+ self.num2 + Calculator.num

obj = Calculator(2,3)
obj.getData()
print(obj.Summation())