class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map1=set(nums1)
        map2=set(nums2)
        lst=[]
        for num in map1:
            if num in map2:
                lst.append(num)
        return lst

