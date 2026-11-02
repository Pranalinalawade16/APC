def reverse_string(string):
    rev=string[::-1]
    return rev

def reverse_with_loop(string):
    rev=" "
    for i in string:
        rev=i+rev
    return rev
name=input("enter string:")
print(reverse_string(name))
print(reverse_with_loop(name))

