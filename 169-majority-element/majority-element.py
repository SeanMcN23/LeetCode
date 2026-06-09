class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        myMap={}

        for x in nums:
            myMap[x] = myMap.get(x,0) + 1
     
        return max(myMap, key=myMap.get)