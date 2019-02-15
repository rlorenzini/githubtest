#input number, print all divisors

num = int(input("Enter Whole Number: "))
#num is what we want to divide

divisor_range = list(range(1,num+1))
#where we start and where we end (0-num)
divisors = []
#divisors will hold the list of divisors applicable to num

for number in divisor_range: #takes 0-num and assigns it to number
    if num % number == 0: #divides input by number
        divisors.append(number) #if no remainder adds to array


print(divisors) #print array list
