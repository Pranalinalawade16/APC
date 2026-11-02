s=input("enter  a string:")
frequency={}

for ch in s:
    if ch in frequency:
        frequency[ch]+=1
    else:
        frequency[ch]=1

print("frequency of every char:")

for ch , count in frequency.items():
    print(ch,":",count)
