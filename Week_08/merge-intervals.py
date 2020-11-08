#56. 合并区间
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])  #以区间起始位进行升序排序
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:   #res为空或者res最新区间的末尾元素小于当前比较区间的起始元素，证明不重合
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res
