
class Solution:
    def countPrimes(self, n: int) -> int:
        is_prime = [True for _ in range(n)]
        res = 0
        for i in range(2, n):
            if is_prime[i]:
                res += 1
                j = i * i
                while j < n:
                    is_prime[j] = False
                    j += i
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.countPrimes(10))
