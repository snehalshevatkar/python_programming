DivisibleBy5=lambda no:(no%5==0)

def main():
    Value=int(input("enter number:"))
    Result=DivisibleBy5(Value)
    print("divisible by 5:",Result)
    
if __name__=="__main__":
    main()    