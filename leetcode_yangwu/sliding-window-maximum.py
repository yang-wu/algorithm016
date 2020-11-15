#239. 滑动窗口最大值
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        result = []
        for i, num in enumerate(nums):
            if deque and deque[0] <= i - k:
                deque.popleft()
            while deque and nums[deque[-1]] < num:
                deque.pop()
            deque.append(i)
            if i >= k - 1:
                result.append(nums[deque[0]])
        return result
