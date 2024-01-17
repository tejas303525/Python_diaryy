class longest_substr:
    def lenth_longest_substr(self,s):
        charset=set()
        l,res=0,0
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            
            charset.add(s[r])
            res=max(res,r-l+1)
        return res



solution=longest_substr()
print(solution.lenth_longest_substr("abcabcbb"))
