class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map=set()

        for x in nums:

            if x in map:
                return True
            map.add(x)

        return False
        
        
        