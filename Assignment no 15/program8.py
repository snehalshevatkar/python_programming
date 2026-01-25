Divisible=lambda no:(no%3==0 and no % 5==0)

def main():
    data=[10,15,30,45,22,9]
    print("actual data is:",data)
    
    result=list(filter(Divisible,data))
    print("divisible by 3 and 5 :",result)
    
if __name__=="__main__":
    main()    