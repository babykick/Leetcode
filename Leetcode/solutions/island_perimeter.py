'''
https://leetcode.com/problems/island-perimeter/#/description

Problem:
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
    
Example:
[[0,1,0,0],

 [1,1,1,0],

 [0,1,0,0],

 [1,1,0,0]]



Answer: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:

:author: babykick
:date: 2017-04-10
'''


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        get_near = lambda i, j: grid[i][j] if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) else 0
        offset = (0, 1), (0, -1), (-1, 0), (1, 0) 
        # total num of borders of all land square - repeation count border num
        total = sum(grid[i][j] for i in range(len(grid)) for j in range(len(grid[0]))) * 4
        #print('total', total)
        rep = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    #print('check', i, j)
                    # check around
                    for dx, dy in offset:
                        if get_near(i + dy, j + dx) == 1:
                            #print('near', i + dy, j + dx)
                            rep += 1
        #print('rep', rep)             

        return total - rep
        


if __name__ == '__main__':
    test_cases = [
        # tuple of (input, output)
        ([[0,1,0,0],
         [1,1,1,0],
         [0,1,0,0],
         [1,1,0,0]], 16),
    ]
    
    for sample in test_cases:
        inp, outp = sample
        assert(Solution().islandPerimeter(inp) == outp)
    
