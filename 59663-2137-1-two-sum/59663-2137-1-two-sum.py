class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset={}

        for index, n in enumerate(nums):
            temp=target-n
            if temp in hashset:
                return (hashset[temp],index)
            hashset[n] = index
               
           
       
            
        