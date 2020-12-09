from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        num2cnt = dict()
        for task in tasks:
            num2cnt[task] = num2cnt.get(task, 0) + 1
        num2cnt = sorted(num2cnt.items(), key=lambda key: -key[1])
        if n == 0:
            res = len(tasks)
        elif num2cnt[0][1] > len(tasks) // 2:
            res = (num2cnt[0][1] - 1) * (n + 1) + 1
        else:
            res = (num2cnt[0][1] - 1) * (n + 1) + 1
            for _, val in num2cnt[1:]:
                if val == num2cnt[0][1]:
                    res += 1
                else:
                    break
        return max(len(tasks), res)


if __name__ == '__main__':
    solution = Solution()
    tasks = ["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"]
    n = 2
    print(solution.leastInterval(tasks, n))
