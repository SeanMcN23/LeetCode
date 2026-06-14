# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def helper(cp,cq):

            if not cp and not cq:
                return True
            
            if not cp or not cq or cp.val != cq.val:
                return False
            return helper(cp.left,cq.left) and helper(cp.right,cq.right)
        return helper(p,q)
        

