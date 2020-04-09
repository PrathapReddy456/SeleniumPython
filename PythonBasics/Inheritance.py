from PythonBasics.OopsDemo import Calculator

class inheritance (Calculator):
    num12= 200
    def __init__(self):
        Calculator.__init__(self,2,10)
    def getCompleteData(self):
        return self.num12 + self.num + self.Summation()

obj1=inheritance()
print(obj1.getCompleteData())