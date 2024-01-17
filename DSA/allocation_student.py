class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def books(self, A, B):
		def isallocation(barrier):
			pages=0
			allocated_student=1
			for i in A:
				if i > barrier:
					return False
				if i+pages > barrier:
					allocated_student+=1
					pages+=i
				else:
					pages+=i
			if allocated_student>B:
				return False
			else:
				return True	
			
		
		
		low=min(A)
		high=sum(A)
		res=0
		while low<=high:
			mid=low+(high-low)//2
			if (isallocation(mid)):
				high=mid-1
				res=mid
			else:
				low=mid+1
		
		return res
        
solution=Solution()

print(solution.books([12,34,67,90],2))