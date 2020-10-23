#127. 单词接龙
from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0
        n = len(beginWord)
        hashword = defaultdict(list)
        for word in wordList:
            for i in range(n):
                hashword[word[:i] + "*" + word[i+1:]].append(word)
        queue = [(beginWord, 1)]
        visited = {beginWord: True}
        while queue:
            curword, level = queue.pop(0)
            for i in range(n):
                matchword = curword[:i] + "*" + curword[i+1:]
                for word in hashword[matchword]:
                    if word == endWord:
                        return level + 1
                    if word not in visited.keys():
                        visited[word] = True
                        queue.append((word, level + 1))
                #hashword[matchword] = []
        return 0
