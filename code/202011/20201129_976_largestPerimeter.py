from typing import List


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A = sorted(A)
        cur_idx = len(A) - 1
        while cur_idx >= 2:
            if A[cur_idx] < A[cur_idx - 1] + A[cur_idx - 2]:
                return sum(A[cur_idx - 2:cur_idx + 1])
            else:
                cur_idx -= 1
        return 0


if __name__ == '__main__':
    solution = Solution()
    A = [3, 2, 3, 4]
    print(solution.largestPerimeter(A))
