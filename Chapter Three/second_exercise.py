# Create Program to Allow user give movie ticket if user name with start A or a letter with age above 10
name = input("Please enter name: ").lower()
age = int(input("Please enter age: "))

if name[0] == 'a' and age > 9:
    print("Coming")
else:
    print("Not Allow")