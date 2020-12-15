#1133. 最大唯一数
class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        hashA = {}
        for a in A:
            if a not in hashA.keys():
                hashA[a] = 1
            else:
                hashA[a] += 1
        maxNum = -1
        for key, val in hashA.items():
            if val == 1:
                maxNum = max(maxNum, key)
        return maxNum
