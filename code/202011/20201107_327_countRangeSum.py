from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        l = len(nums)
        res = 0
        for i in range(l):
            cur_val = nums[i]
            if lower <= cur_val <= upper:
                res += 1
            for j in range(i + 1, l):
                cur_val += nums[j]
                if lower <= cur_val <= upper:
                    res += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    nums = [-2, 5, -1]
    lower = -2
    upper = 2
    print(solution.countRangeSum(nums, lower, upper))
