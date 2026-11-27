"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """

        def solve(r, c, size):

            val = grid[r][c]
            same = True

            for i in range(r, r + size):
                for j in range(c, c + size):
                    if grid[i][j] != val:
                        same = False
                        break
                if not same:
                    break

            if same:
                return Node(val == 1, True, None, None, None, None)

            half = size // 2

            topLeft = solve(r, c, half)
            topRight = solve(r, c + half, half)
            bottomLeft = solve(r + half, c, half)
            bottomRight = solve(r + half, c + half, half)

            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)

        return solve(0, 0, len(grid))
        