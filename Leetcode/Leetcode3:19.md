[TOC]

# 1. Leetcode 53（DP）

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

**Example:**

```
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

很简单的DP思路的题，和之前的找乘积最大的子串思路类似，是一个简化版的。

- 由之前的最大数值和当前数值相加，并且和当前的数值比较；
- 如果小于那么说明在之前的最大数值加上这个数有提升，如果小于那么说明之前的是负数此数为正数。将最大值保存为当前数值；

```java
class Solution {
    public int maxSubArray(int[] nums) {
        int size = nums.length;
        if(size < 1) {
            return 0;
        }
        if(size == 1) {
            return nums[0];
        }
        int res = nums[0];
        int max = nums[0];
        for(int i = 1;i < size;i++) {
            max = Math.max(max+nums[i],nums[i]);
            res = Math.max(max,res);
        }
        return res;  
    }
}
```

# 2. Leetcode 279（DP）

Given a positive integer *n*, find the least number of perfect square numbers (for example, `1, 4, 9, 16, ...`) which sum to *n*.

**Example 1:**

```
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
```

给定一个数字n，使得这个数字可以被最少的平方数加和返回平方数的个数。

这道题还是DP的思路：

- 一个数N可以被平方数加和得到，这个平方数最大只能是$n = ((int)\sqrt N)^2$ (对开平方取整数再平方)；
- 所以相当于我们就是要找到从 1 到 $\sqrt n$ 的这些数字使得他们的平方加和为目标N；
- 利用DP的思路就是，找到从1到N中的每一个数字可以被平方数加和得到的需要的最少的平方数的数量；
- 每一个dp[i]代表的就是要组成 i 需要的最少的平方数的数量；

```java
class Solution {
    public int numSquares(int n) {
        int[] dp = new int[n+1];
        Arrays.fill(dp,Integer.MAX_VALUE);
        for(int i = 1;i <= n;i++) {
            int sqrt = (int)Math.sqrt(i);
            if(sqrt * sqrt == i) {
                dp[i] = 1;
                continue;
            }
            for(int j = 1;j <= sqrt;j++) {
                int temp = i - j*j;
                dp[i] = Math.min(dp[i],dp[temp] + 1);
            }
        }
        return dp[n]; 
    }
}
```

# 3. Leetcode 5（STRING）

Given a string **s**, find the longest palindromic substring in **s**. You may assume that the maximum length of **s** is 1000.

**Example 1:**

```
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
```

找到最长的回文子串，判断回文子串的方式主要从两个方面：

- 首先是如果整个字符串是奇数的那么判断回文从中间出发向两边扩散；
- 如果是偶数的那就左右不在同一点出发，因为需要第一个点就得比对；

首先注意substring的使用，其次是中心点从整个字符串的第一个位置开始出发知道最后一个点的前一个就可以（减少一个点的遍历。。。）substring的第二个参数是不包含的。。

```java
class Solution {
    public int maxLength,start;
    public String longestPalindrome(String s) {
        int size = s.length();
        if(size < 2) {
            return s;
        }
        for(int i = 0;i < size;i++) {
            extendString(s,i,i);
            extendString(s,i,i + 1);
        }
        return s.substring(start,start + maxLength);          
    }
    public void extendString(String s,int left,int right) {
        while(left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        if(maxLength < right - left - 1) {
            maxLength = right - left - 1;
            start = left + 1;
        }
    }
}
```

