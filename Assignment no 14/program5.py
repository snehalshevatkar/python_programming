checkeven=lambda no:(no%2==0)

def main():
    Value=int(input("enter number:"))
    Result=checkeven(Value)
    print("it is even:",Result)
    
if __name__=="__main__":
    main()    