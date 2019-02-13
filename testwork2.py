#ask user for a number
#determine if odd or even
#let user know if number is / by 4

no1 = int(input("Enter Whole Number: "))

if no1 % 2 == 0:
    print("EVEN!")
if no1 % 4 == 0:
    print("Divisible by four!!!!")
else:
    print("Odd one out!")


first_name = input("Enter Your First Name: ")
last_name = input("Enter Your Last Name: ")
print(f"Your name is {first_name} {last_name}.")
