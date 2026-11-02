def replace_char(s):
    old="e"
    new="i"
    result=""
    for ch in s:
        if ch==old:
            result+=new
        else:
            result+=ch
    return result
    

s=input("Enter a string:")
a=s.replace("a","o")
print(a)
n=input("enter a string:")
print(replace_char(n))
