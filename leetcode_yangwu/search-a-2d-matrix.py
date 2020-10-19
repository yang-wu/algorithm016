#74. 搜索二维矩阵
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        mleft = 0
        mright = m - 1
        while mleft <= mright:
            mmid = (mleft + mright) // 2
            if target == matrix[mmid][0] or target == matrix[mmid][n-1]:
                return True
            elif target < matrix[mmid][0]:
                mright = mmid - 1
            elif matrix[mmid][0] < target < matrix[mmid][n-1]:
                break
            else:
                mleft = mmid + 1
        nleft = 0
        nright = n - 1
        while nleft <= nright:
            nmid = (nleft + nright) // 2
            if target == matrix[mmid][nmid]:
                return True
            elif target < matrix[mmid][nmid]:
                nright = nmid - 1
            else:
                nleft = nmid + 1
        return False
