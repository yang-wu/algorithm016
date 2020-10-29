#190. 颠倒二进制位
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        step = 31
        while n:
            res += (n & 1) << step  #通过n & 1每次取最后一位值，左移step位实现反转
            n = n >> 1    #n每次右移1位，等价于逆序遍历
            step -= 1     #左移步长step每次减一，等价于逆序反转
        return res
            
