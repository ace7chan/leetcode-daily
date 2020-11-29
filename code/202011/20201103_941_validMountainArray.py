from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        i = 1
        while i < len(A) and A[i] > A[i - 1]:
            i += 1
        if i == 1 or i == len(A):
            return False
        while i < len(A) and A[i] < A[i - 1]:
            i += 1
        if i != len(A):
            return False
        return True


if __name__ == '__main__':
    solution = Solution()
    A = [0, 3, 2, 1]
    print(solution.validMountainArray(A))