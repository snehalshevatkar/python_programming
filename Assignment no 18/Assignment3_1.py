def sum_list(lst):
    total=0
    for i in lst:
        total+=i
    return total  

no=int(input("enter number of elements:"))
lst=[]

for i in range(no):
    ele=int(input())
    lst.append(ele)
    
print("addition of all elements:",sum_list(lst))     