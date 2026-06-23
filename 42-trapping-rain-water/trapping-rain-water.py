class Solution:
    def trap(self, height: List[int]) -> int:
        # so this problem is in need of the 2 pointer system

        # I need a result, a l, and r pointer
        l,r= 0, len(height)-1
        result=0
        leftMax,rightMax= height[l],height[r]

        

        while l < r:

            if leftMax < rightMax:
                l += 1
                leftMax=max(height[l],leftMax)
                result += leftMax-height[l]
            else:
                r -= 1
                rightMax=max(height[r],rightMax)
                result += rightMax-height[r]
        return result

        