"""
TODO
"""
from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums = self.radix_sort(nums)
        res = 0
        for i, val in enumerate(nums[1:]):
            res = max(abs(val - nums[i]), res)
        return res

    def radix_sort(self, nums):
        RADIX = 10
        maxLength = False
        tmp, placement = -1, 1
        while not maxLength:
            maxLength = True
            buckets = [list() for _ in range(RADIX)]
            for i in nums:
                tmp = i // placement
                buckets[tmp % RADIX].append(i)
                if maxLength and tmp > 0:
                    maxLength = False  # 只要存在一个数非False, 就继续

            a = 0
            for b in range(RADIX):
                buck = buckets[b]
                for i in buck:
                    nums[a] = i
                    a += 1
            # move to next digit
            placement *= RADIX
        return nums


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 6, 9, 1]
    print(solution.maximumGap(nums))
