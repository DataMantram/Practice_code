'''
10. Write a program to print multiplication table of n using for loops in reversed 
order.
'''
n = int(input("Enter the table Range: "))
for i in range(1, 11):
    a = 11-i
    print(f"{n}X{a} = {n*a}")
    