
from functools import reduce
multiply=lambda a,b:a*b

def main():
    data=[1,2,3,4]
    print("actual data is:",data)
    
    result=reduce(multiply,data)
    print("product of all elements is:",result)
    
if __name__=="__main__":
    main()    