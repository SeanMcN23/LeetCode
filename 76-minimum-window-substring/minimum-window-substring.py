class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        tCount= {}

        for c in t:
            tCount[c]=1+tCount.get(c,0)
        
        windowL={}

        have,need= 0, len(tCount)
        resLen, res= [-1,-1], float("infinity")
        l=0

        for r in range(len(s)):
            c=s[r]
            windowL[c]= 1+windowL.get(c,0)

            if c in tCount and tCount[c] == windowL[c]:
                have += 1

            while have >= need:
                # update the win con now

                if(r-l+1) < res:
                    resLen= [l,r]
                    res= r-l+1
                
                # now we need to remove an l and shift the lens
                windowL[s[l]] -= 1

                if s[l] in tCount and windowL[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1
        l, r = resLen
        return s[l : r + 1] if resLen != float("infinity") else ""
        
