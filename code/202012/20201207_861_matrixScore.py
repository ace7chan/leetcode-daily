from typing import List


class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        row, col = len(A), len(A[0])
        res = 0
        for i in range(row):
            if A[i][0] == 0:
                A[i] = [1 - a for a in A[i]]
        res += pow(2, col - 1) * row
        for j in range(1, col):
            one_num = sum([1 == A[i][j] for i in range(row)])
            if one_num >= (row + 1) // 2:
                res += pow(2, col - j - 1) * one_num
            else:
                res += pow(2, col - j - 1) * (row - one_num)
        return res


if __name__ == '__main__':
    solution = Solution()
    A = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
    print(solution.matrixScore(A))
