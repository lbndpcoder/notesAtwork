[TOC]

# 1. Leetcode 32

Given a string containing just the characters `'('` and `')'`, find the length of the longest valid (well-formed) parentheses substring.

**Example 1:**

```
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
```

**Example 2:**

```
Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
```

## solution 1. \<stack>

##solution 2. \<DP>

用 DP 的解法就是说只有三种情况：

- 在当前的位置是 " ( " 的情况，无论如何都是以当前的位置为结尾的合理的括号的长度都是0；
- 如果当前位置是 " ) " 的情况：
  - 前一个位置是 " ( "，那么在前两个位置为结尾的组成的最长的长度+2；
  - 如果前一个长度也是 " ( "，判断前两个位置是不是存在，如果存在，判断上一个位置是否存在并且是不是当前的另一半 " ) "， 如果存在那么当前的位置还需要加上上一个截断位置；不存在那么只需要上一个位置的长度+2；如果上一个位置的位置的另一半不存在那么说明这是一个孤立的截断，所以为0；

```java
class Solution {
    public int longestValidParentheses(String s) {
        int size = s.length();
        if(size == 0) return 0;
        int[] dp = new int[size];
        dp[0] = 0;
        int max = 0;
        for(int i = 1;i < size;i++) {
            char temp = s.charAt(i);
            if(temp == '(') dp[i] = 0;
            if(temp ==  ')' && s.charAt(i - 1) == '(') {
                if(i >= 2) {
                    dp[i] = dp[i - 2] + 2;
                }else {
                    dp[i] = 2;
                }
            }
            if(temp == ')' && s.charAt(i - 1) == ')') {
                if(i - dp[i - 1] - 1 >= 0 && s.charAt(i - dp[i - 1] - 1) == '(') {
                    if(i - dp[i - 1] - 2 >= 0) {
                        dp[i] = dp[i - dp[i - 1] - 2] + dp[i - 1] + 2;
                    }else {
                        dp[i] = dp[i - 1] + 2;
                    }
                }else {
                    dp[i] = 0;
                }
            }
            max = Math.max(max,dp[i]);
        }
        return max;
    }
}
```

