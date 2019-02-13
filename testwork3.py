#take a list of ten numbers
#write a program to print out all numbers >= 5
a = [1,3,5,6,4,2,5,6,78,3]

num = int(input("Choose a number: "))

new_list = []


for i in a:
    if i < num:
        new_list.append(i)

print(new_list)
