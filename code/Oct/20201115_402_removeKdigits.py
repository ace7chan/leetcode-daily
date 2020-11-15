class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        res, idx = [], 0
        cur_val = num[0]
        while k > 0 and idx < len(num):
            if len(res) == 0 or cur_val >= res[-1]:
                res.append(cur_val)
                idx += 1
                cur_val = num[idx] if idx < len(num) else None
            else:
                res.pop()
                k -= 1
        res.extend(num[idx:])
        while k > 0 and len(res) > 0:
            res.pop()
            k -= 1
        return str(int(''.join(res) if len(res)>0 else 0))


if __name__ == '__main__':
    solution = Solution()
    num = "1234567890"
    k = 9
    print(solution.removeKdigits(num, k))
