name=input("Enter a string:")
print("Lenght of string:",len(name))
vowel=0
consanat=0
space=0
special=0
digit=0
for i in name:
    if i=="a" or i=="e" or i=="o" or i=="u" or i=="i":
        vowel+=1
    elif i==" ":
        space+=1
    elif i=="!" or i=="@" or i=="#" or i=="$" or i=="%" or i=="^" or i=="&" or i=="*" or i=="~" :
        special+=1
    elif i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9" or i=="0":
        digit+=1
    else:
        consanat+=1

print(f"Count of  vowel:{vowel} \n Count of consanats:{consanat} \n Count of space:{space} \n Count of special Charater:{special} \n Count of digit:{digit}")
