class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        myhash={}
        scout,res=0,0
        highest=0

        for scout in range(len(s)):
            myhash[s[scout]] = 1 + myhash.get(s[scout],0)

            while (scout-res+1)-max(myhash.values()) > k :
                myhash[s[res]] -= 1
                res += 1

            
            
            highest= max(highest,scout-res+1)
        return highest
        

      