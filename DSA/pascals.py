# r-1 C c-1 where r and c are row and colum
def nCr(n,r):
    n=n-1
    r-r-1
    res=1
    for i in range(r):
        res=res*(n-i)
        res=res//(i+1)
    return res

# variant 2
def printrow(n):
    for col in range(1,n+1):
        print(nCr(n-1,col-1),end=" ")

# variant3
def printPascal(n):
    ans=[]
    for row in range(1,n+1):
        temp=[]
        for col in range(1,row+1):
            temp.append(nCr(row-1,col-1))
        ans.append(temp)
        for row in ans:
            for eke in row:
                print(eke,end=" ")
        
if __name__=="__main__":
    print("1st variant answer ",nCr(int(input("enter row number ")),int(input("Enter col number "))))
    print(" ")
    print("2nd variant answer ")
    printrow(int(input("Enter the row u want to print ")))
    print(" ")
    print("3rd variant answer ")
    printPascal(int(input("num of rows ")))
