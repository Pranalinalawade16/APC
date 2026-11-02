s=input("Enter a string:")
upper=0
lower=0
print("length",len(s))
for i in s:
    if i.islower():
        lower+=1
    elif i.isupper():
        upper+=1
    else:
        pass
print(f"Count of lowercase:{lower} and uppercase:{upper}")
