class Solution:

    def tree(self, n):
        for i in range(1, n + 1):
            print(("*" * (i * 2 - 1)).center(15))


n = int(input())
Solution().tree(n)