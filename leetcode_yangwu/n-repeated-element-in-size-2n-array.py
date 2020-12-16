#961. 重复 N 次的元素
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        hashA = {}
        n = len(A)
        for a in A:
            if a not in hashA.keys():
                hashA[a] = 1
            else:
                hashA[a] += 1
        for key, val in hashA.items():
            if val == n // 2:
                return key
