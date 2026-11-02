def palindrome_string(string):
    original=string
    rev=string[ : :-1]
    return rev==original

def palindrome(string):
    original=string
    rev=" "
    for i in string:
        rev=i+rev
    return rev==original



name=input("Enter a string:")
a=palindrome_string(name)
if a is True:
    print("Palindrome")
else:
    print("Non-palindrome")

z=input("Enter a string:")
b=palindrome(z)
if b is True:
    print("Palindrome")
else:
    print("Non-palindrome")
