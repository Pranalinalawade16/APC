sen=input("Enter a sentences:")
word=sen.split()
count=len(word)
print("Count of words:",count)
print(word)



#longest word in sentence
sen1=input("Enter a sentences:")
word1=sen1.split()
longest=""
for word in word1:
   if len(word)>len(longest):
            longest=word

print("Longest word :",longest)



#shortest word in sentence
sen2=input("Enter a sentences:")
word2=sen1.split()
smallest=""
for word in word2:
   if len(word)<len(smallest):
            smallest=word

print("Smallest word :",smallest)
