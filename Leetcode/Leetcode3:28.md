[TOC]

# 1. Leetcode 329

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

**Example 1:**

```
Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
```

找到在一个矩阵当中的最长的递增路径：

- 遍历所有的矩阵中的点；
  - 从每一个点出发利用 dfs ；
  - 分别到达当前点的四个方向：如果越过边界或者当前点的数值小于下一个点的数值；
  - 在每个方向上都更新当前点的最大的路径长度；
  - 并且存储每一个点的出发的最大路径长度，如果遇到这个已经遍历过的点直接返回当前点的数值；

```java
class Solution {
    public static int[][] dirs = {{0,1},{1,0},{0,-1},{-1,0}};
    public int longestIncreasingPath(int[][] matrix) {
        int r = matrix.length;
        if(r <= 0) {
            return 0;
        }
        int c = matrix[0].length;
        int[][] visited = new int[r][c];
        int max = 0;
        for(int i = 0;i < r;i++) {
            for(int j = 0;j < c;j++) {
                int res = dfs(matrix,r,c,i,j,visited);
                max = Math.max(max,res);
            }
        }
        return max;
    }
    public int dfs(int[][] matrix,int r,int c,int i,int j,int[][] visited) {
        if(visited[i][j] != 0) {
            return visited[i][j];
        }
        int max = 1;
        for(int[] dir:dirs) {
            int x = i + dir[0];
            int y = j + dir[1];
            if(x < 0 || x >= r || y < 0 || y >= c || matrix[x][y] <= matrix[i][j]) {
                continue;
            }
            int path = 1 + dfs(matrix,r,c,x,y,visited);
            max = Math.max(path,max);
        }
        visited[i][j] = max;
        return max;
    }
}
```

# 2. Leetcode 127 (BFS)

Given two words (*beginWord* and *endWord*), and a dictionary's word list, find the length of shortest transformation sequence from *beginWord* to *endWord*, such that:

1. Only one letter can be changed at a time.
2. Each transformed word must exist in the word list. Note that *beginWord* is *not* a transformed word.

**Note:**

- Return 0 if there is no such transformation sequence.
- All words have the same length.
- All words contain only lowercase alphabetic characters.
- You may assume no duplicates in the word list.
- You may assume *beginWord* and *endWord* are non-empty and are not the same.

**Example 1:**

```
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
```

这个题的说明就很长，大概的意思就是：

- 又一个字典字典里面的字符串的长度是一定长度的；
- 给定一个初始的字符串，每一次变换一个字符，变换后的字符串必须在字典中；
- 要求变换的最少的次数；（如果存在变换至少变换**一次**）；

所以整体的思路就是：

- 设置一个队列，首先将 beginWord 加入队列当中；
- 每一次分别弹出队列中的元素，弹出一个元素，分别对这个字符串中的每一个字符进行替换（26个字母）；
- 如果替换之后的字符串在字典中并且没有被访问过就说明可能是通过这个字符串变换得到的 endWord；

利用的是 queue 并且是 BFS，访问的每一层都是当前 word 变换一次才能变成的字符串保证了最少的次数；

并且细节代码上利用了hashSet add( )方法；并且在替换之后生成新的String，并且在替换入队列之后要换回来；

```java
class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Set<String> hs = new HashSet<>(wordList);
        if(!hs.contains(endWord)) {
            return 0;
        }
        int minLength = 0;
        Queue<String> qu = new LinkedList<>();
        Set<String> visited = new HashSet<>();
        qu.offer(beginWord);
        visited.add(beginWord);
        while(!qu.isEmpty()) {
            int size = qu.size();
            minLength += 1;
            for(int i = 0;i < size;i++) {
                String word = qu.poll();
                if(word.equals(endWord)) {
                    return minLength;
                }else {
                    char[] wordArray = word.toCharArray();
                    for(int j = 0;j < wordArray.length;j++) {
                        char preChar = wordArray[j];
                        for(char start = 'a';start <= 'z';start++) {
                            wordArray[j] = start;
                            String newWord = new String(wordArray);
                            if(hs.contains(newWord) && !visited.contains(newWord)) {
                                qu.offer(newWord);
                                visited.add(newWord);
                            }
                        }
                        wordArray[j] = preChar;
                    }
                }
            }
        }
        return 0;
    }
}
```

