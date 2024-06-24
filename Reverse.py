Write a program that will reverse a four digit number.Also it checks whether the reverse

Step 1 

x = input("Enter 4 digit number: ")
y = x[::-1]

if x == y:
    print(True)
else:
    print(False)
