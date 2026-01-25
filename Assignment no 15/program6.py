
from functools import reduce
minimum=lambda a,b:a if a<b else b

def main():
    data=[1,2,3,4,5]
    print("actual data is:",data)
    
    result=reduce(minimum,data)
    print("minimum is:",result)
    
if __name__=="__main__":
    main()    