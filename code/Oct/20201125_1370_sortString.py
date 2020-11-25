class Solution:
    def sortString(self, s: str) -> str:
        char2num = dict()
        for c in s:
            char2num[c] = char2num.get(c, 0) + 1
        key_inc = sorted(char2num)
        key_dec = key_inc[::-1]
        flag = True
        res = []
        while len(char2num) > 0:
            key_name = key_inc if flag else key_dec
            for key in key_name:
                if key not in char2num:
                    continue
                res.append(key)
                char2num[key] -= 1
                if char2num[key] == 0:
                    char2num.pop(key)
            flag = not flag
        return ''.join(res)


if __name__ == '__main__':
    s = "aaaabbbbcccc"
    solution = Solution()
    print(solution.sortString(s))
