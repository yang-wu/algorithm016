#14. 最长公共前缀
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        m = len(strs)
        n = len(strs[0])
        for j in range(n):
            first = strs[0][j]  #第0行第j列字母
            for i in range(1, m):
                if len(strs[i]) == j or strs[i][j] != first:  #如果第i行的长度等于当前遍历的列数或第i行第j列字母不等于第0行第j列字母
                    return strs[0][:j]   #返回第0行前j-1个字母作为最长公共前缀
        return strs[0]  #如果遍历完成，返回第0行整个单词作为最长公共前缀
