#prime number check

num = int(input("\nGive me a number: \n"))

i = num -1
prime = True
while i > 1:
    if num % i == 0:
        prime = False
    i = i-1

if prime == True:
    print("\nPRIME.\n")
if prime == False:
    print("\nNOT PRIME.\n")
