def max_list(lst):
    return max(lst)

n=int(input("enter number of elements:"))
lst=[]

for i in range(n):
    ele=int(input())
    lst.append(ele)
    
print("maximum elements:",max_list(lst))    