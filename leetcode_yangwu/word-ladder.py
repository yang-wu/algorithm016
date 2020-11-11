#127. 单词接龙
from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0
        m = len(beginWord)
        hashWord = defaultdict(list)
        for word in wordList:
            for i in range(m):
                hashWord[word[0:i] + "*" + word[i+1:m]].append(word)
        queue = [(beginWord, 1)]  #队列保存访问单词和当前长度的元组
        visited = {beginWord: True}
        while queue:
            curWord, level = queue.pop(0)
            for i in range(m):
                for word in hashWord[curWord[0:i] + "*" + curWord[i+1:m]]: #遍历模糊匹配单词列表是否是结尾单词
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        queue.append((word, level + 1))
                        visited[word] = True
        return 0

