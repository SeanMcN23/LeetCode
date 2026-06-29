class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map= {}

        for index,num in enumerate(nums):
            rem=target-num
            if rem in map:
                return [map[rem],index]

            
            else:
                map[num] = index
        return -1
            
            



               
           
       
            
        