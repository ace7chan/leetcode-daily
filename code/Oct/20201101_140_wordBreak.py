from typing import List

# 这道题比较恶心的地方就在于aaaaabaa这类型情况, 可以先提前判断每个字符是否都存在
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        char2pos = dict()
        total_char = set()
        self.res = []
        for w in wordDict:
            if w[0] not in char2pos:
                char2pos[w[0]] = [(len(w), w)]
            else:
                char2pos[w[0]].append((len(w), w))
            for c in w:
                total_char.add(c)
        # 先判断当前字符串里的每个字符是否都在字典中
        for c in s:
            if c not in total_char:
                return self.res
        self.s = s
        self.total_len = len(s)
        self.char2pos = char2pos
        self.helper(0, [], 0)
        return self.res

    def helper(self, pos, temp_list, cur_len):
        if cur_len == self.total_len:
            self.res.append(' '.join(temp_list))
            return
        if pos < self.total_len and self.s[pos] in self.char2pos:
            cnt = 0
            for l, word in self.char2pos[self.s[pos]]:
                if word == self.s[pos:pos + l]:
                    cnt += 1
                    temp_list.append(word)
                    cur_len += l
                    self.helper(pos + l, temp_list, cur_len)
                    temp_list.pop()
                    cur_len -= l
            if cnt == 0:
                return
        else:
            return


if __name__ == '__main__':
    solution = Solution()
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    print(solution.wordBreak(s, wordDict))
