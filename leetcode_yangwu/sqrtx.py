#69. x 的平方根
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid - 1
            else: 
                left = mid + 1
                if left * left == x:
                    return left
                elif left * left > x:
                    return mid
        
