n=int(input("enter n"))
original=n
reverse=0
while n>0:
  digit=n%10
  reverse=reverse*10+digit
  n=n//10
if original==reverse:
  print("pallindrome")
else:
  print("not pallindrome")
