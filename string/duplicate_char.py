str=input("Enter a string:")
dup=""
for ch in str:
    if str.count(ch)>1 and ch not in dup:
            dup+=ch

print("Duplicate characters:",dup)
