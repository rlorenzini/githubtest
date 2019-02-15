#list compression; display only even; one line of code

numbers = [1,2,3,4,5,6,7,8,9,0]
even_numbers = [even for even in numbers if even % 2 == 0]

print(even_numbers)

#array2 = [element for element in array1 if element % 2 == 0]



#years = [1991,1992,1993,1994,1995]
#age = []
#for year in years: #applying this function
#    age.append(2019 - year)
#print(age)
#age = [2019 - year for year in years] #into a list compression
#print(age)
