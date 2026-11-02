s=input("Enter a string")

first=0
second=0
first_char=""
second_char=""

for ch in s:
    count=s.count(ch)

    if count>first:
        second=first
        second_char=first_char
        first=count
        first_char=ch
    elif count>second and count!=first:
        second=count
        second_char=ch

print("Second highest frequency char:",second_char)
print("It's frequency:",second)
