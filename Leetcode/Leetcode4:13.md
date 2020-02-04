[TOC]

# 1. Leetcode 583（String，DP）

Given two words *word1* and *word2*, find the minimum number of steps required to make *word1* and *word2* the same, where in each step you can delete one character in either string.

**Example 1:**

```
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
```

这道题的意思是怎么删除两个字符串中的字符才能使得两个字符串相同并且要求次数最少；可以理解成为找到两个字符串中的最长的子串；

利用DP的思想（套路），设置2维矩阵：

- 如过当前的字符相同说明dp\[i][j]  = dp\[i - 1][j - 1] + 1;
- 如果当前不同说明是和"上一层"或者退后一步比较；
  - 上一层是没有这个字符加入的时候这个位置的最长子串的长度；
  - 后退一步是加入这个字符之后的字符在上一个位置上的最长子串长度；

```java 
class Solution {
    public int minDistance(String word1, String word2) {
        int[][] dp = new int[word1.length() + 1][word2.length() + 1];
        int i = 1;int j = 1;
        for(char w1:word1.toCharArray()) {
            j = 1;
            for(char w2:word2.toCharArray()) {
                if(w1 == w2) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                }else {
                    dp[i][j] = Math.max(dp[i - 1][j],dp[i][j - 1]);
                }
                j++;
            }
            i++;
        }
        int dup = dp[word1.length()][word2.length()];
        return word1.length() + word2.length() - 2*dup;
    }
}
```

# 2. Leetcode 718（DP，array）

Given two integer arrays `A` and `B`, return the maximum length of an subarray that appears in both arrays.

**Example 1:**

```
Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1].
```

和上面的题可以说是很相似了，这个题主要是要找到的是连续的相同子序列；

- 只考虑的是"对角线”；
  - DP的思想是每一次增加一个元素去找到在另一个序列中的匹配的序列长度；
  - 每次匹配的时候只考虑连续情况；dp\[i - 1][j - 1]  大小；

```java
class Solution {
    public int findLength(int[] A, int[] B) {
        int[][] dp = new int[A.length + 1][B.length + 1];
        int i = 1;int j = 1;
        int max = 0;
        for(int a:A) {
            j = 1;
            for(int b:B) {
                if(a == b) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                    max = Math.max(max,dp[i][j]);
                }
                j++;
            }
            i++;
        }
        return max;
    }
}
```

# 3. Leetcode 187（String，Hash）

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

**Example:**

```
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
```

找到长度为10的子串并且这个连续的子串出现的次数要大于1次：

- 利用两个 HashSet：
  - 一个用来判断是不是出现过；
  - 一个用来存储出现过的子串；
- 利用substring每一次提取长度为10 的子串；

```java
class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        HashSet<String> seen = new HashSet<>();
        HashSet<String> repeated = new HashSet<>();
        for(int i = 0;i < s.length() - 9;i++) {
            String sub = s.substring(i,i + 10);
            if(!seen.add(sub)) {
                repeated.add(sub);
            }
        }
        return new ArrayList<String>(repeated);
    }
}
```

# SUMMARY

今天的三道题，前两个题属于一个思路的类型，都是利用DP的思想解决最长字符串的问题：

- 第一个题解决的是不连续的字符串的匹配问题，所以要比较"上一层"和"退一步"；
- 第二个问题解决的是连续的问题，所以只需要比较"对角线"上的问题；

第三个题是一个滑动窗口的问题：

- 利用的一个substring找到每一个长度为10的String，利用两个HashSet判断是不是出现过；

和 300 题进行对比；