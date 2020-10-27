#547. 朋友圈
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        visited = [0 for i in range(len(M))]
        count = 0
        for i in range(len(M)):
            if visited[i] == 0:    #遍历visited数组，遍历的轮数即为朋友圈数量（如果全部为朋友，第一轮所有元素都置为1，只会遍历一轮）
                self.dfs(M, visited, i)
                count += 1
        return count

    def dfs(self, M, visited, i):
        for j in range(len(M)):
            if M[i][j] == 1 and visited[j] == 0: #遍历visited数组，如果i和j是朋友且j未被遍历，置j位为1
                visited[j] = 1
                self.dfs(M, visited, j)
        
