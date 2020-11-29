from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        p1, p2 = 0, 1
        p_start, p_len = 0, len(A)
        while p1 < p_len and p2 < p_len and p_start < p_len:
            if A[p_start] % 2 == p_start % 2:
                p_start += 1
            elif A[p_start] % 2 == 0:
                A[p_start], A[p1] = A[p1], A[p_start]
                p1 += 2
            else:
                A[p_start], A[p2] = A[p2], A[p_start]
                p2 += 2
        return A


if __name__ == '__main__':
    solution = Solution()
    A = [2, 3]
    print(solution.sortArrayByParityII(A))
