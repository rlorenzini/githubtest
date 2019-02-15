#two lists (arrays)
#random numbers (input, generated, or pre-defined)
#check for overlapping numbers

list_one = [1,2,3,2,6554,7,8,999,0]
list_two = [1,2,3,5,6,6778,999,87765,21]
list_three = []
for number in list_one:
    if number in list_two:
        list_three.append(number)
print(list_three)
