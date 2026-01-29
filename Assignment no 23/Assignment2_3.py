class Numbers:
    
    def __init__(self):
        self.Value = int(input("Enter Number: "))
    
    def ChkPrime(self):
        if self.Value < 2:
            return False
        for i in range(2, int(self.Value**0.5)+1):
            if self.Value % i == 0:
                return False
        return True
    
    def ChkPerfect(self):
        sum_factors = self.SumFactors()
        return sum_factors == self.Value
    
    def Factors(self):
        print("Factors:", end=" ")
        for i in range(1, self.Value+1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()
    
    def SumFactors(self):
        sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum += i
        return sum


# Multiple objects
N1 = Numbers()
N1.Factors()
print("Prime:", N1.ChkPrime())
print("Perfect:", N1.ChkPerfect())

print("----------------")

N2 = Numbers()
N2.Factors()
print("Prime:", N2.ChkPrime())
print("Perfect:", N2.ChkPerfect())
