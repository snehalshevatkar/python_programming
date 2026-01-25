checkodd=lambda no:(no%2!=0)

def main():
    Value=int(input("enter number:"))
    Result=checkodd(Value)
    print("it is odd:",Result)
    
if __name__=="__main__":
    main()    