# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the
# # digits

#step 1 : write a program to accept an integer and print in reverse order

x = input("enter the number: ")
y = x[::-1]

#step 2: Insert a space to separate the digits 

k = " ".join(y)
print(k)
