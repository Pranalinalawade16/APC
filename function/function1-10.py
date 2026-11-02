def factorial(num):
    n=num

    if n==1:
        return 1
    else:
        n=n*factorial(n-1)
        return n

print(factorial(3))

def even_odd(n):
    if n%2==0:
        print("This is Even number")
    else:
        print("This is Odd number")
    
even_odd(7)

def greater_num(a,b):
    if a>b:
        print(a,"is greater than",b)
    else:
        print(b,"is greater than",a)

greater_num(89,72)

def simple_interset(p,r,t):
    return p*r*t/100
s=simple_interset(10000,5,1)
print(s)

def is_prime(n):
    if n<2:
        return False

    for i in range(2,n):
        if n%i==0:
            return False
        return True
print(is_prime(8))
print(is_prime(7))

def area_circle(r):
    return 2*3.14*r
print(area_circle(4))

def sum_n(n):
    sum=0
    for i in range(n+1):
        sum+=i
    return sum
print(sum_n(5))

def power(base,exponent):
     result=1
     for i in range(exponent):
         result*=base
     return result
print(power(2,3))

def max(nums):
    max=0
    for i in nums:
        if i>max:
            max=i
    return max
nums=[12,78,94,24,56,34]
print(max(nums))

def vowels(s):
    string=s.split(",")
    count=0
    for i in string:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" :
            count+=1
    return count
s="Abhi is in the lab"
print(vowels(s))
