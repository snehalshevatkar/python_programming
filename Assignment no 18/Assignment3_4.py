

n=int(input("enter number of elements:"))
lst=[]

print("enter elements:")
for i in range(n):
    lst.append(int(input()))
    
search=int(input("enter elements to search:"))

print("list:",lst)
print("frequency of",search,"is:",lst.count(search))    