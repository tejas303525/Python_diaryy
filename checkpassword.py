password="796115110113721110141108"

password=password[::-1]
i=0
res=""
while (i<len(password)-1):
    x=password[i]+password[i+1]
    if int(x)==32:
        res+=chr(int(x))
    elif int(x) in range(65,91) or int(x)in range(97,123):
        res+=chr(int(x))
    elif i+2 < len(password):
        x+=password[i+2]
        res+=chr(int(x))
        i+=1
    i+=2
print(res)
