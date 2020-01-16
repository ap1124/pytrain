str1 = input("Enter a string: ")
str2 = input("Enter an another string: ")

str3 = str1 +" "+str2

print(f"To upper: {str3.upper()} \nTo Lower: {str3.lower()} \nTitle case: {str3.title()}")

str4 = "String"
str4 = str4.join(str1.split())

print(str4.center(30, '$'))
