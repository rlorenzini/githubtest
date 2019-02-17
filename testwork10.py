#make two lists of different len()
#take out common numbers
#place common numbers in third list and print

list1 = [1,3,5,7,9,11,13,15,17,19]
list2 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
list3 = []

for value in list1:
    for value2 in list2:
        if value == value2:
            list3.append(value)
print(list3)
