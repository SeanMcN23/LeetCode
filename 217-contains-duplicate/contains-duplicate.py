class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset=set()
        for x in nums:
            if x in hashset:
                return True
            else:
                hashset.add(x)
        return False
        
        
        