#palindrome
word = input("\nEnter Word Here: \n").lower()

def reverse(word):
    return word[::-1]
def palindrome(word):
    rev = reverse(word)
    if word == rev:
        return True
    return False

result = palindrome(word)
if result == True:
    print("\nPalindrome.\n")
else:
    print("\nNot palindrome.\n")









user_input = input("\nEnter Word Here:\n").lower()

def reverse(user_input):
    return user_input[::-1]
def testing(user_input):
    if user_input == reverse(user_input):
        return True
    return False
returned = testing(user_input)
if returned == True:
    print("\nPalindrome.\n")
else:
    print("\nNot palindrome.\n")
