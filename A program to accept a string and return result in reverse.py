
name = str(input("Enter your name: "))
reverse_name = name[::-1]

# Add a space in between the reversed name 
for_db = " ".join(reverse_name)
print(for_db)
