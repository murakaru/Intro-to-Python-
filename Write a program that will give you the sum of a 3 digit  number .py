x = int(input("Enter a three digit number : "))

y = str(x)
# Case - check the number of digits
input_length = len(y)

if input_length != 3:
    print("Please enter 3 digit number")
else:
    a = x%10
    num = x//10
    b = num%10
    c = num//10
    print(a+b+c)

