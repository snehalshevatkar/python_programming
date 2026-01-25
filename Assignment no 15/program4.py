
from functools import reduce
add=lambda a,b:a+b

def main():
    data=[1,2,3,4,5]
    print("actual data is:",data)
    
    result=reduce(add,data)
    print("addition is all elements:",result)
    
if __name__=="__main__":
    main()    