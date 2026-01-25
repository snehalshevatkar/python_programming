maximum=lambda a,b:a if a>b else b

def main():
   no1=int(input("enter 1st number:"))
   no2=int(input("enter 2nd number:"))
   
   result=maximum(no1,no2)
   print("maximum is:",result)
   
if __name__=="__main__":
    main()    