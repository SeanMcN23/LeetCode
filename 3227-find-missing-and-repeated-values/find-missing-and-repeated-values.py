class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        map={}

        # inputs: a grid, or a list of list with int inputs, each number should appear exactly once except a that appears twice, and b that does not appear

        for x in grid:
            for y in x:
                map[y] = map.get(y,0) + 1

        a,b= 0,0
        for x in range(len(grid)**2):
            real=x+1
            if real in map and map[real] == 2:
                a=real
            if real not in map:
                b=real
            if a != 0 and b != 0:
                break
        return [a,b]


        