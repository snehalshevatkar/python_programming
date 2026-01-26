def sum_factors(n):
    s=0
    for i in range(1,n):
        if n % i == 0:
         s=s+i
    return s    
     
num=int(input("enter number:"))
print("sum of factors:",sum_factors(num))     