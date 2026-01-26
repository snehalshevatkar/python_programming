def min_list(lst):
    return min(lst)

n=int(input("enter number of elements:"))
lst=[]

for i in range(n):
    ele=int(input())
    lst.append(ele)
    
print("minimum elements:",min_list(lst))    