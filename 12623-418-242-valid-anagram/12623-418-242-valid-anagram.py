class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myHash1={}
        myHash2={}
        if len(s) != len(t):
            return False
        for char in s:
            if char in myHash1:
                myHash1[char] += 1
            else:
                myHash1[char] = 1
        for char in t: 
            if char in myHash2:
                myHash2[char] += 1
            else:
                myHash2[char] = 1
        for element in myHash1:
            if element not in myHash2:
                return False
            else:
                if myHash1[element] != myHash2[element]:
                    return False
        return True
        
