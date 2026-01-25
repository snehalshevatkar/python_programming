
from functools import reduce
maximum=lambda a,b:a if a>b else b

def main():
    data=[1,2,3,4,5]
    print("actual data is:",data)
    
    result=reduce(maximum,data)
    print("maximum :",result)
    
if __name__=="__main__":
    main()    