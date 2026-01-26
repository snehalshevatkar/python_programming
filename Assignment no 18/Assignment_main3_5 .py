import Assignment_marvellous3_5

n=int(input("enter number of elements:"))
lst=[]

print("enter elements:")
for i in range(n):
    lst.append(int(input()))
    
sumprime=0
for num in lst:
    if Assignment_marvellous3_5.chekprime(num):  
        sumprime+=num
        
print("sum of prime numbers",sumprime)          