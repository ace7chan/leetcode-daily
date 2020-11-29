from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_tuple = [(n, i) for i, n in enumerate(nums)]
        nums_tuple = sorted(nums_tuple, key=lambda key: key[0])
        res = [0 for _ in nums]
        for i, num in enumerate(nums_tuple):
            if i == 0 or (num[0] != nums_tuple[i - 1][0]):
                res[num[1]] = i
            else:
                res[num[1]] = res[nums_tuple[i - 1][1]]
        return res


if __name__ == '__main__':
    solution = Solution()
    nums = [8, 1, 2, 2, 3]
    print(solution.smallerNumbersThanCurrent(nums))
