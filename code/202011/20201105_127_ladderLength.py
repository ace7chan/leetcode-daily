from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        stack1 = [beginWord]
        stack2 = []
        step = 1
        visited = {w: False for w in wordList}
        char_list = [chr(ord('a') + i) for i in range(26)]
        while len(stack1) != 0 or len(stack2) != 0:
            if len(stack1) == 0:
                stack1 = stack2
                stack2 = []
                step += 1
            cur_word = stack1.pop()
            for i in range(len(cur_word)):
                for j in range(26):
                    if char_list[j] == cur_word[i]:
                        continue
                    tmp_word = cur_word[:i] + char_list[j] + cur_word[i + 1:]
                    if tmp_word in wordSet and not visited[tmp_word]:
                        if tmp_word == endWord:
                            return step + 1
                        stack2.append(tmp_word)
                        visited[tmp_word] = True
        return 0


if __name__ == '__main__':
    solution = Solution()
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    beginWord = "hit"
    endWord = "cog"
    print(solution.ladderLength(beginWord, endWord, wordList))
