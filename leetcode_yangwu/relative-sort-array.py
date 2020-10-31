#1122. 数组的相对排序
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        cnt = collections.Counter(arr1)  #等价于Hash计数
        for i in arr2:
            if cnt[i]:
                res.extend([i] * cnt[i])  #根据arr2元素对新数组排序
                cnt.pop(i)    #从计数列表中不断删除已经排好的元素，剩下的元素为arr1和arr2差异元素
        for i in range(1001):  #题目数组长度最大不超过1001，变相等价于按序遍历剩余的计数器列表
            if cnt[i]:
                res.extend([i] * cnt[i])
        return res
