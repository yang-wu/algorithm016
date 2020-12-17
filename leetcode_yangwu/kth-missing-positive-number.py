#1539. 第 k 个缺失的正整数
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        hashArr = {}
        for i in range(1, 2001):
            hashArr[i] = 0
        for a in arr:
            if a in hashArr.keys():
                hashArr[a] = 1
        count = 0
        for key, val in hashArr.items():
            if val == 0:
                count += 1
            if count == k:
                return key


