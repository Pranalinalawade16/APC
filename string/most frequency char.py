s=input("Enter string:")

max_char=""
max_count=0

for ch in s:
    count=s.count(ch)

    if count>max_count:
        max_char=ch
        max_count=count

print("Char with highest frequency:",max_char)
print("It's frequency:",max_count)
