[TOC]

#1. Leetcode 516（回文子串：5*）

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

**Example 1:**
Input: 

```
"bbbab"
```

Output: 

```
4
```

One possible longest palindromic subsequence is "bbbb".

这道题和第5题的不同在于这道题取到的最长的子串不一定是连续的，利用的是Dp的思想：

- 主要的思想就是判断最两侧的字符是否相同如果相同就可以用内部的子串的最长子串长度加2；
- 如果不相同说明当前的子串的最长回文一定在"便左侧"或"便右侧"的子串中；
- 整个计算都是在一个dp[][]矩阵当中的：

$$
dp[i][j] = dp[i + 1][j - 1] + 2 \\
dp[i][j] = Math.max(dp[i + 1][j],dp[i][j - 1])
$$

```java
class Solution {
    public int longestPalindromeSubseq(String s) {
        int size = s.length();
        int[][] dp = new int[size][size];
        for(int i = 0;i < size;i++) {
            dp[i][i] = 1;
        }
        for(int i = size - 1;i >= 0;i--) {
            for(int j = i + 1;j < size;j++) {
                if(s.charAt(i) == s.charAt(j)) {
                    dp[i][j] = dp[i + 1][j - 1] + 2;
                }else {
                    dp[i][j] = Math.max(dp[i + 1][j],dp[i][j - 1]);
                }
            }
        }
        return dp[0][size - 1];
    }
}
```

在这里再回顾一下第5题（3:19）：

- 主要的思路是找到一个中心点向两侧逐渐寻找相同的，得到 left，right 得到当前的最长长度；
- 根据最终结果的start和 length 用 substring API；注意substring的用法不包含最右侧的点；

# 2. Leetcode 647（回文子串个数）

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

**Example 1:**

```
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
```

和第5题基本一样只是这里每一次找到都要计数的；

```java
class Solution {
    public int count = 0;
    public int countSubstrings(String s) {
        int size = s.length();
        for(int i = 0;i < size;i++) {
            paddle(size,i,i,s);
            paddle(size,i,i + 1,s);
        }
        return count;
    }
    public void paddle(int size,int left,int right,String s) {
        while(left >= 0 && right <= size - 1 && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
            count++;
        }
    }
}
```

# 3. Leetcode 730（巧妙：回文个数）

Given a string S, find the number of different non-empty palindromic subsequences in S, and **return that number modulo 10^9 + 7.**

A subsequence of a string S is obtained by deleting 0 or more characters from S.

A sequence is palindromic if it is equal to the sequence reversed.

Two sequences `A_1, A_2, ...` and `B_1, B_2, ...` are different if there is some `i` for which `A_i != B_i`.

**Example 1:**

```
Input: 
S = 'bccb'
Output: 6
Explanation: 
The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
Note that 'bcb' is counted only once, even though it occurs twice.
```

找到所有的回文子串的个数，这个子串可以是不连续的，主要的思路是分了大体上两个情况

- 如果左右两端的数值不同的话我们可以知道：

$$
dp[i][j] = -dp[i + 1][j - 1] + dp[i][j - 1] + dp[i + 1][j];
$$

- 如果左右两端相同的话那么就会出现三种情况：
  - (1) 如果是“a……a”这种类型的，中间的子串的个数所有情况都可以套上aa再来一遍，并且还需要加上['a','aa']这两种情况；所以：
  - (2) 如果是''a…..a…..a'这种的情况就说明中间的情况已经有“a”这种了所以中间的情况套上aa之后就需要再加上‘’aa‘这种情况就行了；
  - (3) 如果是''‘a….a….a….a'这种情况多个a存在的情况就说明内侧的‘’…..a…..a….‘’这种情况*2之后即使套上外面的aa也重复了；

$$
(1)\quad dp[i][j] = dp[i + 1][j - 1] * 2 + 2 \\
(2)\quad dp[i][j] = dp[i + 1][j - 1] * 2 + 2 \\
(3)\quad dp[i][j] = dp[i + 1][j - 1] * 2 - dp[low + 1][high - 1];
$$

那么如何构建寻找样式的体系呢：

- 从小区间开始寻找，构建distance=1开始遍历一遍把所有距离为distance的求一遍；
- 构建slow和high两个指针：slow从i开始找，high从j开始往回找；
  - 如果slow找到和两侧相同的数值并且slow > high 说明是"a…..a";
  - 如果slow和high相同说明都找到中间"a…a…a";
  - 如果slow < high说明是"a…a….a….a";

```java
class Solution {
    public int countPalindromicSubsequences(String S) {
        int length = S.length();
        int[][] dp = new int[length][length];
        for(int i = 0;i < length;i++) {
            dp[i][i] = 1;
        }
        char[] a = S.toCharArray();
        for(int distance = 1;distance < length;distance++) {
            for(int i = 0;i < length - distance;i++) {
                int j = i + distance;
                if(a[i] == a[j]) {
                    int low = i + 1;
                    int high = j - 1;
                    while(low <= high && a[low] != a[j]) {
                        low++;
                    }
                    while(low <= high && a[high] != a[j]) {
                        high--;
                    }
                    if(low > high) {
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 2;
                    }else if(low == high) {
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 1;
                    }else {
                        dp[i][j] = dp[i + 1][j - 1] * 2 - dp[low + 1][high - 1];
                    }
                }else {
                    dp[i][j] = -dp[i + 1][j - 1] + dp[i][j - 1] + dp[i + 1][j];
                }
                dp[i][j] = dp[i][j] < 0?dp[i][j] + 1000000007:dp[i][j] % 1000000007;
            }
        }
        return dp[0][length - 1];  
    }
}
```

关于

```java
 dp[i][j] = dp[i][j] < 0?dp[i][j] + 1000000007:dp[i][j] % 1000000007;
```

可以证明在 a > b , a%M - b%M < 0 的情况下有：
$$
(a-b)\% M = a \% M - b\%M + M;
$$
所以由于在过程中求余导致做差为负数其实是为了求差的余，所以利用这个公式；