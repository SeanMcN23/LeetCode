class Solution:
    def maxArea(self, height: List[int]) -> int:
        highest=0
        temp=0
        temp2=0
        temp3=0

        left=0
        right=len(height)-1

        while left< right:
            temp=right-left
            temp2=min(height[left], height[right])
            temp3= temp*temp2

            if temp3> highest:
                highest=temp3
            if height[left]<height[right]:
                left +=1
            elif height[right]<height[left]:
                right -= 1

            else:
                right -=1
        return highest
        
             
            
        