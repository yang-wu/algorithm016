#905. 按奇偶排序数组
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        n = len(A)
        i = 0
        j = n - 1
        while i < j:  #双指针夹逼算法
            if A[i] % 2 == 0 and A[j] % 2 == 0:
                i += 1
            elif A[i] % 2 == 0 and A[j] % 2 == 1:
                j -= 1
            elif A[i] %  2 == 1 and A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
            else:
                j -= 1
        return A
