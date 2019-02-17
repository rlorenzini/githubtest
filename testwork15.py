test = "This is just a bunch of words."
result = test.split(" ")
# print(result)

def backwards(a):
    b = a.split(" ")

    b.reverse()
    c = " ".join(b)
    return c
result = backwards(test)
print(result)
