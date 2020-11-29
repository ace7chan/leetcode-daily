from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        one_num, connect_num = 0, 0
        row, col = len(grid), len(grid[0])
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    one_num += 1
                    # 左边连接的情况
                    if r - 1 >= 0 and grid[r - 1][c] == 1:
                        connect_num += 1
                    # 上边连接的情况
                    if c - 1 >= 0 and grid[r][c - 1] == 1:
                        connect_num += 1
        # 每一次连接相当于去除了两条边
        return one_num * 4 - 2 * connect_num


if __name__ == '__main__':
    solution = Solution()
    arr = [[0, 1, 0, 0],
           [1, 1, 1, 0],
           [0, 1, 0, 0],
           [1, 1, 0, 0]]
    print(solution.islandPerimeter(arr))
