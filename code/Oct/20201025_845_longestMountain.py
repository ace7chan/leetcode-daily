from typing import List


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        left, mid, right = 0, 0, 0
        n, res = len(A), 0
        while left < n:
            # 寻找升序
            mid = left
            while mid < n - 1 and A[mid + 1] > A[mid]:
                mid += 1
            if mid == left:
                left = mid + 1
                continue
            # 寻找降序
            right = mid
            while right < n - 1 and A[right + 1] < A[right]:
                right += 1
            if right == mid:
                left = right + 1
                continue
            res = max(res, right - left + 1)  # 左右两边都是闭集合
            left = right
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestMountain([2, 1, 4, 7, 3, 2, 5]))
