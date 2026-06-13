class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        myHash={}
        scout,res=0,0
        highest=0

        for scout in range(len(s)):

             # need to add character to map, then check to see if k- max value is bigger then the whole
            # window i have, which i believe is (s-r)+1

            if s[scout] in myHash:
                myHash[s[scout]] += 1
            else:
                myHash[s[scout]] = 1
            while (scout-res)+1 - max(myHash.values()) > k:
                myHash[s[res]] -= 1
                res += 1

            highest= max (highest, (scout-res)+1)
        return highest
            



          

        

      