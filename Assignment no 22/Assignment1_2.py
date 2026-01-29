class Circle:
    PI = 3.14   # class variable
    
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0
    
    def Accept(self):
        self.Radius = float(input("Enter Radius: "))
    
    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius
    
    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius
    
    def Display(self):
        print("Radius =", self.Radius)
        print("Area =", self.Area)
        print("Circumference =", self.Circumference)
        print("-------------------")


# Creating multiple objects
C1 = Circle()
C1.Accept()
C1.CalculateArea()
C1.CalculateCircumference()
C1.Display()

C2 = Circle()
C2.Accept()
C2.CalculateArea()
C2.CalculateCircumference()
C2.Display()
