class BankAccount:
    ROI = 10.5  
    
    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount
    
    def Display(self):
        print("Account Holder:", self.Name)
        print("Current Balance:", self.Amount)
    
    def Deposit(self):
        amt = float(input("Enter amount to deposit: "))
        self.Amount += amt
    
    def Withdraw(self):
        amt = float(input("Enter amount to withdraw: "))
        if amt <= self.Amount:
            self.Amount -= amt
        else:
            print("Insufficient Balance!")
    
    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest


# Creating object
B1 = BankAccount("Snehal", 5000)
B1.Display()

B1.Deposit()
B1.Display()

B1.Withdraw()
B1.Display()

print("Interest =", B1.CalculateInterest())
