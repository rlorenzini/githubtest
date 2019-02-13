user_name = input("Enter Your Name: ")
user_age = int(input("Enter Your Age: "))

def calcage(a):
    result = (2019 - a) + 100
    return result

year = calcage(user_age)


print(f"Hello, {user_name}! You will be 100 years old in {year}!")
