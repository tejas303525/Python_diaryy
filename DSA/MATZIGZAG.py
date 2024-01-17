def solution(n, arr):
     
    for i in range(len(arr)):
        if i%2==0:
            for j in range(len(arr[i])):
                print(arr[i][j], end="")
        else:
            while j >=0:
                print(arr[i][j],end="")
                j-=1
      
    
def main():
    n = int(input())
    
    arr = []
    
    for i in range(n):
       temp = input().split(" ")
       for j in range(n):
         temp[j] = int(temp[j])
        
       arr.append(temp)
    
    solution(n, arr)

main()
