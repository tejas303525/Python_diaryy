
class solution:
   def __init__(self,n=int(input("Enter a number "))):
      self.n=n
   def weird_algo(self):
      n=self.n
      res=[n]
      while n!=1:
         if n%2==0:
            n=n//2
            res.append(n)
         else:
            n=n*3+1
            res.append(n)
      return res


Solution=solution()
print(Solution.weird_algo())