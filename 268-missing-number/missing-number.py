class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        mySet= set()

        for x in nums:
            mySet.add(x)
        
        for counter in range(len(nums)):
            if counter in mySet:
                continue
            else:
                return counter
        return len(nums)

        