password=input("Enter passwaord:")

upper=lower=digit=special=False

for ch in password:
    if ch.isupper():
        upper=True
    elif ch.islower():
        lower=True
    elif ch.isdigit():
        digit=True
    else:
        special=True

if len(password)>=8 and lower and upper and digit and special:
    print("Valid password")
else:
    print("Invalid password")
