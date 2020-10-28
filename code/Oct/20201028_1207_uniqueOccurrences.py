from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt_dict = dict()
        for v in arr:
            cnt_dict[v] = cnt_dict.get(v, 0) + 1
        return len(set(cnt_dict.values())) == len(cnt_dict.values())


if __name__ == '__main__':
    solution = Solution()
    arr = [1, 1, 2, 3, 3]
    print(solution.uniqueOccurrences(arr))
