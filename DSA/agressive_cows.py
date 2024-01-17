class Solutions:
    def cow(self,arr,c):
        def canPlaced(arr,mid,cows):
            cntCows=1
            lastcow=arr[0]
            for i in range(len(arr)):
                if arr[i]-lastcow >=mid:
                    cntCows+=1
                    lastcow=arr[i]
            return cntCows >= cows

        low,high=0,arr[-1]
        while low<=high:

            mid=low+(high-low)//2
            if canPlaced(arr,mid,c):
                low=mid+1
                

            else:
                high=mid-1
        return high 
        


solution=Solutions()
print(solution.cow([0,3,4,7,9,10],4))