from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []
        res = [[1]]
        for i in range(1, numRows):
            line = [1]
            for j in range(1, i):
                line.append(res[i - 1][j - 1] + res[i - 1][j])
            line.append(1)
            res.append(line)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.generate(1))
