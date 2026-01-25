largest=lambda a,b,c:a if(a>b and a>c) else (b if b>c else c)

def main():
   no1=int(input("enter 1st number:"))
   no2=int(input("enter 2nd number:"))
   no3=int(input("enter 3rd number:"))
   
   result=largest(no1,no2,no3)
   print("largest is:",result)
   
if __name__=="__main__":
    main()    