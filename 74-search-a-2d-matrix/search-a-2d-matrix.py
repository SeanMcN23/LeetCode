class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for index,nums in enumerate(matrix):
            l=0
            r=len(matrix[index])-1

            while l <= r:
                m= (r+l) //2

                if matrix[index][m] > target:
                    r=m-1
                elif matrix[index][m]< target:
                    l=m+1
                else:
                    return True
        return False

        