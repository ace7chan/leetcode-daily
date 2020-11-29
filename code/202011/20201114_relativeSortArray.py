from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        val2cnt = {v: 0 for v in arr2}
        left_list = []
        for v in arr1:
            if v in val2cnt:
                val2cnt[v] += 1
            else:
                left_list.append(v)
        res = []
        for v, cnt in val2cnt.items():
            res.extend([v] * cnt)
        res.extend(sorted(left_list))
        return res


if __name__ == '__main__':
    solution = Solution()
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    print(solution.relativeSortArray(arr1, arr2))
