fname = input("Enter first name: ")
lname = input("Enter last name: ")
age = int(input("Enter your age: "))
salary = int(input("Enter your salary: "))

name = fname + " "  + lname
print(name)

print(f"{name[3]} {name[-3]}")

bin_age = bin(age)
bin_salary = bin(salary)
print(bin_age,bin_salary)

print(type(name),type(age),type(salary))

print(ord(fname[0]),ord(lname[0]))
