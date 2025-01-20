class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        s=re.sub(r'[^a-z0-9]','',s.lower())
     
       
        

        for index, x in enumerate(s):
            temp=s[index]
            temp2=s[len(s)-index-1]
            if temp != temp2:
                
                return False
        return True
            

        
       

        
        