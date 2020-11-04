from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        flag = True
        for interval in intervals:
            # 1. 没有交集的情况
            if interval[1] < newInterval[0]:
                res.append(interval)
            elif interval[0] > newInterval[1]:
                if flag:
                    res.append(newInterval)
                    flag = False
                res.append(interval)
            else:
                # 2. 必然有交集的情况
                if newInterval[0] <= interval[0] and newInterval[1] >= interval[1]:
                    continue
                elif interval[0] <= newInterval[0] and interval[1] >= newInterval[1]:
                    res.append(interval)
                    flag = False
                    continue
                elif newInterval[0] > interval[0]:
                    newInterval[0] = interval[0]
                elif newInterval[1] < interval[1]:
                    newInterval[1] = interval[1]
        if flag:
            res.append(newInterval)
        return res


if __name__ == '__main__':
    solution = Solution()
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    print(solution.insert(intervals, newInterval))
