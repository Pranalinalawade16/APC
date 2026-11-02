n=int(input("how namy numbers"))
i=1
smallest=int(input("enter number"))
while i<n:
  num=int(input("enter number"))
  if num<smallest:
    smallest=num
  i=i+1
print("Smallest number=",smallest)
