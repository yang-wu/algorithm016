class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashNum = {}
        for num in nums:
            hashNum[num] = hashNum[num] + 1 if num in hashNum.keys() else 1
        heapNum = []
        for key, count in hashNum.items():
            if len(heapNum) < k:
                heapq.heappush(heapNum, (count, key))
            else:
                heapq.heappushpop(heapNum, (count, key))
        arrayNum = []
        for num in heapNum:
            arrayNum.append(num[1])
        return arrayNum

