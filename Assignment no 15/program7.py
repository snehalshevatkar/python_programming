

checklength=lambda S:len(S)>5

def main():
    data=["python","java","c","sql","angular"]
    print("actual data is:",data)
    
    result=list(filter(checklength,data))
    print("string length is>5 :",result)
    
if __name__=="__main__":
    main()    