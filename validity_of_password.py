def isValid(password):
    if len(password) > 8 and len(password) < 15:
        if any(i!=" " for i in password):
            if any(i.isupper() for i in password):
                if any(i.islower() for i in password):
                    if any(i.isdigit() for i in password):
                        if any(i in ['$', '#', '@'] for i in password):
                            return True




password1 = "GeeksForGeeks"
 
if (isValid([i for i in password1])):
    print("Valid Password")
else:
    print("Invalid Password!!!")
 
password2 = "Geek$ForGeeks7"
if (isValid([i for i in password2])):
    print("Valid Password")
else:
    print("Invalid Password!!!")