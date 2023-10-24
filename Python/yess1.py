#password = input ("what is your password ")
#password = ("me")
attempts = 0

while attempts != 3:
    password= input("enter password ")
    attempts = attempts + 1

    if password == ("me"):
        break
    else:
        print("wrong  ")

    if attempts >3: 
        break 
    else :
        print("password incorect")

if password == ("me"):
    print("welcome ")
else:
     print("locked out ")