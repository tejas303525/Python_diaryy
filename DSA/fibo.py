def fibo(n):
    if n>=1:
        return n*fibo(n-1)
    else:
        return 1
print(fibo(int(input("Enter your number: "))))
