class Arithmetic:
    
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
    
    def Accept(self):
        self.Value1 = int(input("Enter Value1: "))
        self.Value2 = int(input("Enter Value2: "))
    
    def Addition(self):
        return self.Value1 + self.Value2
    
    def Subtraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        if self.Value2 == 0:
            return "Division by zero not allowed"
        else:
            return self.Value1 / self.Value2


# Multiple objects
A1 = Arithmetic()
A1.Accept()
print("Addition =", A1.Addition())
print("Subtraction =", A1.Subtraction())
print("Multiplication =", A1.Multiplication())
print("Division =", A1.Division())
print("-------------------")

A2 = Arithmetic()
A2.Accept()
print("Addition =", A2.Addition())
print("Subtraction =", A2.Subtraction())
print("Multiplication =", A2.Multiplication())
print("Division =", A2.Division())
