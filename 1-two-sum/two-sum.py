class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}

        for index,x in enumerate(nums):
            if target-x in map:
                return index,map[target-x]
            else:
                map[x]=index
        
               
           
       
            
        