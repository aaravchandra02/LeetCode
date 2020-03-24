"""Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 

Return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
Example 3:

Input: grid = [[1,-1],[-1,-1]]
Output: 3
Example 4:

Input: grid = [[-1]]
Output: 1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100
"""

import numpy as np


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return (np.array(grid) < 0).sum()

    def countNegatives_2(self, grid: List[List[int]]) -> int:
        n = np.matrix(grid)
        return(np.count_nonzero(n < 0))

    def countNegatives_efficient(self, grid: List[List[int]]) -> int:
        # as the matrix is in descending order
        m, n = len(grid), len(grid[0])
        r, c, cnt = m - 1, 0, 0
        # checking from bottom left
        while r >= 0 and c < n:
            if grid[r][c] < 0:
                cnt += n - c
                r -= 1
            else:
                c += 1
        return cnt
