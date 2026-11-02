s=input("Enter a sting:")
a=input("Enter a char to find:")
count=0
for ch in s:
    if ch==a:
        count+=1

print("Number of occurrence:",count)
