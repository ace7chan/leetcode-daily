from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr = sorted(arr, key=lambda key: (sum([int(i) for i in bin(key)[2:]]), key))
        return arr


if __name__ == '__main__':
    solution = Solution()
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print(solution.sortByBits(arr))
