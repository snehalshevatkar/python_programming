
square=lambda no:no*no

def main():
    data=[1,2,3,4,5]
    print("actual data is:",data)
    
    result=list(map(square,data))
    print("square:",result)
    
if __name__=="__main__":
    main()    