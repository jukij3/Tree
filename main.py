class Solution:
    def levels(i):
        print(("*" * (i*2-1)).center(15))
    def tree(n):
        # input(n)
        for i in range(1, n+1):
            Solution.levels(i)

n = int(input())
Solution.tree(n)