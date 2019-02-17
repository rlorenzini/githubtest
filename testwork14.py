num = [1,1,2,2,3,4,5,6,7,7,8,9,0]
num = set(num)
num = list(num)
# print(num)
potatoes = ["yes","no","yes","potato"]

def listingarrays(a):
    a = set(a)
    a = list(a)
    return a
result = listingarrays(num)
print(result)
result2 = listingarrays(potatoes)
print(result2)
