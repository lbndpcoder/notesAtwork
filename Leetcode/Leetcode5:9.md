[TOC]

# Leetcode 10

Given an input string (`s`) and a pattern (`p`), implement regular expression matching with support for `'.'` and `'*'`.

```
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
```

The matching should cover the **entire** input string (not partial).

**Note:**

- `s` could be empty and contains only lowercase letters `a-z`.
- `p` could be empty and contains only lowercase letters `a-z`, and characters like `.` or `*`.

**Example 1:**

```
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```

这个题的主要意思就是正则的匹配，规则如下：

- 如果当前的为"*"说明可以重复n次前面的字符；
  - 可以重复无限次数；
  - 可以去掉前面的字符；
- 如果当前的字符为"."说明当前的字符可以匹配任何的字符；

利用 Dp 的思路：

- 如果当前是" . "，说明当前可以匹配任意的字符需要看上一个匹配结果；
- 如果当前是"*"：
  - 上一个不是"."并且上一个和当前的匹配不同，说明 * 要消除上一个字符，并且当前的匹配结果依靠的是上上个的匹配结果；

```java
class Solution {
    public boolean isMatch(String s, String p) {
        int m = s.length();
        int n = p.length();
        boolean[][] dp = new boolean[m + 1][n + 1];
        dp[0][0] = true;
        for(int i = 1;i <= n;i++) {
            if(p.charAt(i - 1) == '*') {
                dp[0][i] = dp[0][i - 2];
            }
        }
        for(int i = 1;i <= m;i++) {
            for(int j = 1;j <= n;j++) {
                if(p.charAt(j - 1) == '.') {
                    dp[i][j] = dp[i - 1][j - 1];
                }else if(p.charAt(j - 1) == '*') {
                    if(p.charAt(j - 2) != '.' && s.charAt(i - 1) != p.charAt(j - 2)) {
                        dp[i][j] = dp[i][j - 2];
                    }else {
                        dp[i][j] = dp[i][j - 1] || dp[i][j - 2] || dp[i - 1][j];
                    }
                }else {
                    dp[i][j] = dp[i - 1][j - 1] && s.charAt(i - 1) == p.charAt(j - 1);
                }
            }
        }
        return dp[m][n];
    }
}
```

