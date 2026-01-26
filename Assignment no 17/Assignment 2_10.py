def sum_digits(n):
    s=0
    for digit in str(n):
        s+=int(digit)
    return s

num=int(input("enter number:"))
print("sum of digits",sum_digits(num))    