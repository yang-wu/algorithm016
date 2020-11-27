#67. 二进制求和
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sumab = int(a, 2) + int(b, 2)  #字符串转换为十进制相加
        res = str(bin(sumab))[2:]  #十进制转换为二进制，再转为字符串，去掉二进制前两位标记0b
        return res


