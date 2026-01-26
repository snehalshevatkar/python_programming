def pattern_number_triangle(n):
    for i in range(1,n+1):
        for j in range(1, i+1):
         
         print(j, end=" ")
        print()
        
num=int(input("enter number: "))
pattern_number_triangle(num)        