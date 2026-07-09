class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        res=0
        l,r=0,0
        g.sort()
        s.sort()

        while l < len(g) and r < len(s):
            if s[r] < g[l]:
                r+= 1
            elif s[r] >= g[l]:
                l += 1
                r += 1
                res += 1
        return res
            

