#This is ibm coding round in hackerrank of 2024,
# Create a table to validate passowrd and userid. Use the digit to create palindrome token


def login(Userid,password,digits):
    h={
        "user1":"pass1",
        "user2":"pass2",
        "user3":"pass3",
        "user4":"pass4",
        "user5":"pass5",
    }

    if digits % 2 == 0:
        first_half = str(10**(digits//2 - 1))
        palindrome = int(first_half + first_half[::-1])
    else:
        first_half = str(10**(digits//2))
        palindrome = int(first_half + first_half[:-1][::-1])

    
    
    if h[Userid]==password:
        print("welcome " + str(Userid) + " your token-" + str(palindrome))
    else:
        print("userId or password is wrong")


if __name__=="__main__":
    Userid=input("Enter the Userid: ")
    password=input("Enter the password: ")
    digit=int(input("Enter the digit: "))
    login(Userid,password,digit)