n=int(input("enter n"))
i=2
count=0
while i<n:
  if n%i==0:
    count=count+1
  i=i+1
if n>1 and count==0:
  print("prime number")
else:
  print("Not a prime number")
