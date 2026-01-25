
checkodd=lambda no:(no % 2!=0)

def main():
    data=[11,10,15,20,22,27,30]
    print("actual data is:",data)
    
    result=list(filter(checkodd,data))
    print("checkodd:",result)
    
if __name__=="__main__":
    main()    