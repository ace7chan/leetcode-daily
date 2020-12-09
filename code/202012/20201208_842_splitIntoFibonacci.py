from typing import List


class Solution:
    def is_valid_num(self, S, left, right):
        if right > len(S):
            return False
        if int(S[left:right]) > 2147483647:
            return False
        if S[left] == '0' and right - left > 1:
            return False
        return True

    def is_fibonacci(self, S, i, j):
        first, second = int(S[:i]), int(S[i:j])
        res = [first, second]
        add_num = str(first + second)
        while j < len(S) and add_num == S[j:j + len(add_num)] and self.is_valid_num(S, j, j + len(add_num)):
            j = j + len(add_num)
            first = second
            second = int(add_num)
            res.append(second)
            add_num = str(first + second)
        if j == len(S) and len(res) >= 3:
            return res
        return None

    def splitIntoFibonacci(self, S: str) -> List[int]:
        for i in range(1, 11):
            if not self.is_valid_num(S, 0, i):
                continue
            for j in range(i + 1, i + 11):
                if not self.is_valid_num(S, i, j):
                    continue
                res = self.is_fibonacci(S, i, j)
                if res is None:
                    continue
                else:
                    return res
        return []


if __name__ == '__main__':
    solution = Solution()
    print(solution.splitIntoFibonacci("1101111"))
