class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums2 is the main set, where nums1 is the subset of nums2

        # for each num less than nums1.length, 

        # so nums1 gives us like a list of numbers to go over in nums2,, in nums 2 we need to figure out is there a greater number after that
        myMap={} # so now nums2 is mapped to what is in nums2, IE number to index
        for index,num in enumerate(nums2):
            myMap[num]=index
        
        ans=[]
        check=False
        for num in nums1:
            index=myMap[num]
            for x in range(index,len(nums2)):
                if nums2[x] > num:
                    ans.append(nums2[x])
                    check=True
                    break
            if check is False:
                ans.append(-1)
            check=False
        return ans






        