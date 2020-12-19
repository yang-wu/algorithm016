#剑指 Offer 10- I. 斐波那契数列
from functools import lru_cache
class Solution:
    @lru_cache
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        return (self.fib(n-1) + self.fib(n-2)) % 1000000007
