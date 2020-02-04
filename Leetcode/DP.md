[TOC]

# 53. Maximum Subarray

找到一个数组中连续的数字的和最大是多少，找到状态转移方程：

- 因为是连续的数字的和，所以只能是当前最大的和只能是max（nums[i], dp[i - 1] + nums[i]）；
  - 由当前的数字重新开始，或者和之前的数字加和，判断这两个哪个大；

```java
class Solution {
    public int maxSubArray(int[] nums) {
        if(nums.length == 1) return nums[0];
        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        int res = dp[0];
        for(int i = 1;i < nums.length;i++) {
            dp[i] = Math.max(nums[i], dp[i - 1] + nums[i]);
            if(dp[i] > res) {
                res = dp[i];
            }
        }
        return res;
    }
}
```

# 152. Maximum Product Subarray

​	找到连续的子串使得乘积最大。因为要求是连续的，所以在每一个位置上有两个选择，要么从当前的数字开始重新计算整个数值，要么计算和之前的数字相乘：在和之前数字相乘保存两个数值，一个是最大的，一个是最小的，因为最小的元素可以和当前的一个负数相乘变成当前的一个较大的数；

```java
class Solution {
    public int maxProduct(int[] nums) {
        int[] dp = new int[nums.length];
        int max = nums[0];
        int min = nums[0];
        int res = nums[0];
        for(int i = 1;i < nums.length;i++) {
            int premax = max;
            int premin = min;
            
            max = Math.max(nums[i], Math.max(premax * nums[i], premin * nums[i]));
            min = Math.min(nums[i], Math.min(premax * nums[i], premin * nums[i]));
            
            res = Math.max(res, max);
        }
        return res;
    }
}
```

#300. Longest Increasing Subsequence

​	要求的是给定一个一个数组中的最长的递增子数组是多少，这个问题可以用：

- DP 的思路，找到状态转移方程；
- 遍历一遍数组，构造一个数组，把每一个数用二分的方式找到位置插入排序；

## （1）DP solution

​	遍历每一个位置 i ，并且从数组开始位置到位置 i 分别比较和位置 i 的数值的大小，更新到位置 i 的最长的递增子数组是多长； 
$$
dp[i] = Math.max(dp[j] + 1,dp[i])
$$

```java
class Solution {
    public int lengthOfLIS(int[] nums) {
        if(nums == null || nums.length == 0) return 0;
        int[] dp = new int[nums.length];
        int res = 1;
        Arrays.fill(dp, 1);
        for(int i = 1;i < nums.length;i++) {
            for(int j = 0;j < i;j++) {
                if(nums[i] > nums[j]) {
                    dp[i] = Math.max(dp[j] + 1, dp[i]);
                }
            }
            res = Math.max(res, dp[i]);
        }
        return res;
    }
}
```

时间复杂度O (n^2)

## （2）binary search and insert

​	构造一个数组，将遍历到的数字都插入进去，最终的长度就是我们要求的：

```java
class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] a = new int[nums.length];
        Arrays.fill(a, Integer.MAX_VALUE);
        int count = 0;
        for(int i = 0;i < nums.length;i++) {
            int pos = binary(a, nums[i]);
            a[pos] = nums[i];
            if(pos == count) {
                count++;
            }
        }
        return count;
    }
    public int binary(int[] nums, int target) {
        int l = 0;
        int r = nums.length;
        while(l <= r) {
            int mid = l + (r - l) / 2;
            if(nums[mid] >= target) {
                r = mid - 1;
            }else {
                l = mid + 1;
            }
        }
        return l;
    }
}
```

#5. Longest Palindromic Substring

## （1）DP solution

 	给定一个字符串s，如果判断该字符串的 i 到 j 的位置是回文的，那么有：
$$
f(i,j)=f(i+1,j-1) \quad\&\quad s[i]==s[j]
$$
表示的是第 i+1 个位置到第 j-1 个位置是回文的并且 i 和 j 的位置的字符相同；并且如果位置相差不超过三个，即：“aca” / “bb” / “a” 这种形式，只要求 s[i]==s[j] 就可以满足回文；

![DP](/Users/liubonan/Documents/Leetcode/DP.png)

如图所示，在这个基础上，如果 i 到 j 变成回文，并且长度大于已知的回文子串，那么更新；

```java
class Solution {
    public String longestPalindrome(String s) {
        int len = s.length();
        boolean[][] dp = new boolean[len][len];
        String res = new String();
        for(int i = len - 1;i >= 0;i--) {
            for(int j = i;j < len;j++) {
                dp[i][j] = s.charAt(i) == s.charAt(j) && (j - i < 3 || dp[i+1][j-1]);
                if(dp[i][j] && (j - i + 1 > res.length())) {
                    res = s.substring(i, j+1);
                }
            }
        }
        return res;
    }
}
```

## （2）遍历每一种情况

以每一个字符串中的字符为中心，向两边扩散，进行判断是不是回文的子串，并判断长度了；

```java
class Solution {
    public int max = 0;
    public int st = 0;
    public String longestPalindrome(String s) {
        if(s.length() < 2) return s;
        for(int i = 0;i < s.length();i++) {
            echo(s, i, i);
            echo(s, i, i + 1);
        }
        return s.substring(st, st + max);
    }
    public void echo(String s, int left, int right) {
        while(left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        if(max < right - left -1) {
            max = right - left - 1;
            st = left + 1;
        }
    }
}
```

#123. Best Time to Buy and Sell Stock III

有两次的交易机会，每一次在买入前必须卖出，就是说不能同时进行两次交易，需要有顺序关系：

- 第一次的买入应该是一个比较小的数值，用 buyOne 代表的是如果在当前的股价第一次买入的话，所有的资金，所以如果出现股价比较低的情况就说明此时买入可能是比较好的时候；
- 第一次的卖出，用第一次买入之后的价格加上在此时卖出的价格；
- 第二次买入已经有了一部分的资产，因为第一次卖出；
- 第二次卖出是在第二次买入的基础上；

```java
class Solution {
    public int maxProfit(int[] prices) {
        int size = prices.length;
        if(size < 2) {
            return 0;
        }
        int buyOne = -prices[0];
        int buyTwo = -prices[0];
        int sellOne = 0;
        int sellTwo = 0;
        for(int i = 1;i < size;i++) {
            buyOne = Math.max(buyOne,-prices[i]);
            sellOne = Math.max(sellOne,prices[i] + buyOne);
            buyTwo = Math.max(buyTwo,sellOne - prices[i]);
            sellTwo = Math.max(sellTwo,buyTwo + prices[i]);
        }
        return sellTwo;
        
    }
}
```

# 132. Palindrome Partitioning II

通过切割一个字符串使得切割之后的字符串是回文的最少的切割的次数：

- 遍历整个字符串，在每一个位置，找到以当前位置为结束位置的字符串的最小的切割次数；
- 找到不同的位置之间是否存在回文；
  - 如果存在回文说明切割的次数可以减少；

```java
class Solution {
    public int minCut(String s) {
        int[] min = new int[s.length()];
        boolean[][] p = new boolean[s.length()+1][s.length() + 1];
        for(int i = 0;i < s.length();i++) {
            min[i] = i;
            for(int j = 0;j <= i;j++) {
                if(s.charAt(i) == s.charAt(j) && (j + 1 > i - 1 || p[j+1][i-1])) {
                    p[j][i] = true;
                    min[i] = j == 0?0:Math.min(min[j - 1]+1, min[i]);
                }
            }
        }
        return min[s.length() - 1];
    }
}
```

# 337. House Robber III

​	这个题从一个基本的 DFS 的方法进行不断的优化成为一个比较好的版本（DP的思路）：

## （1）DFS

​	在每一个根节点比较选择此节点打劫或者不打劫的，如果打劫那么在下一个孩子节点的位置直接跳到下一层，如果不打劫，那么继续比较两种情况；

```java
class Solution {
    public int rob(TreeNode root) {
        return helper(root, false);      
    }
    public int helper(TreeNode root, boolean parent) {
        if(root == null) return 0;
        if(parent) {
            return helper(root.left, false) + helper(root.right, false);
        }
        
        return Math.max(helper(root.right, true) + helper(root.left, true) + root.val, 
                       helper(root.right, false) + helper(root.left, false));
    }
}
```

## （2）DP

​	在每一个节点都保存 打劫/不打劫 时的最大的打劫价值，相当于从下到上的递推过程，相比于上面的探索多次打劫不打劫的情况有很大的效率提升；

```java
class Solution {
    public int rob(TreeNode root) {
        int[] res = new int[2];
        res = helper(root);
        return Math.max(res[0], res[1]);
    }
    public int[] helper(TreeNode node) {
        if(node == null) return new int[2];
        
        int[] left = helper(node.left);
        int[] right = helper(node.right);
        
        int[] res = new int[2];
        res[0] = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);
        res[1] = left[0] + right[0] + node.val;
        return res;
    }
}
```

# 188. Best Time to Buy and Sell Stock IV

​	设定一个交易的次数，得到在交易次数内最大的收益：

- 如果设定的次数大于整体天数的一半，说明可以任意的交易；
- 使用一个二维数组的DP思路（滚动数组进行优化）；

# 309. Best Time to Buy and Sell Stock C

​	每一次购买之后都需要“冷静”一天，和之前的购买股票之后卖出不同，此时每一次买入股票需要的不是当前的最大卖出价格而是上一次的最大卖出价格，因为如果当前买入的话是不能利用上一次的最大卖出价格的。

```java
class Solution {
    public int maxProfit(int[] prices) {
        int len = prices.length;
        if(len < 2) return 0;
        int b0 = -prices[0];
        int b1 = b0;
        int s0 = 0;
        int s1 = 0;
        int s2 = 0;
        for(int i = 1;i < len;i++) {
            b0 = Math.max(b1, s2 - prices[i]);
            s0 = Math.max(s1, b1 + prices[i]);
            s2 = s1;
            s1 = s0;
            b1 = b0;
        }
        return s0;
    }
}
```

#72.Edit Distance

更改 word1 中的单词使得可以和 word2 相同最少的修改次数：

```java
class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length();
        int n = word2.length();
        int[] cost = new int[n + 1];
        for(int i = 1;i <= n;i++) {
            cost[i] = i;
        }
        
        for(int i = 1;i <= m;i++) {
            int[] next = new int[n + 1];
            next[0] = i;
            for(int j = 1;j <= n;j++) {
                if(word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    next[j] = cost[j - 1]; 
                }else {
                    int r = cost[j - 1];
                    int ii = next[j - 1];
                    int d = cost[j];
                    int min = (r > d) ? ((d > ii) ? ii:d) : (r > ii ? ii:r);
                    next[j] = min + 1;
                }
            }
            cost = next;
        }
        return cost[n];
    }
}
```

# 91. Decode Ways

​	将一行字符串“1345”编码成为ABCD等的方式有多少，利用 DP 的思路，每一个位置之前的所有的解码方式由两种方式，第一种是位置 i - 1 单独的解码，一种是 i - 2 和 i - 1配合的编码：

```java
class Solution {
    public int numDecodings(String s) {
        int n = s.length();
        int[] dp = new int[n + 1];
        dp[0] = 1;
        dp[1] = s.charAt(0) == '0'?0:1;
        for(int i = 2;i <= n;i++) {
            int f = Integer.valueOf(s.substring(i - 1, i));
            int se = Integer.valueOf(s.substring(i - 2, i));
            
            if(f > 0 && f <= 9) dp[i] += dp[i - 1];
            if(se >= 10 && se <= 26) dp[i] += dp[i - 2];
        }
        return dp[n];
    }
}
```

# 115. Distinct Subsequences

​	DP的思路，如果当前的字符相同，那么说明可以找到去掉当前的字符之前的匹配次数和之前的所有的匹配次数：

```java
class Solution {
    public int numDistinct(String s, String t) {
        int m = s.length();
        int n = t.length();
        
        int[] pre = new int[m + 1];
        for(int i = 0;i <= m;i++) {
            pre[i] = 1;
        }
        for(int i = 0;i < n;i++) {
            int[] cur = new int[m + 1];
            for(int j = 0;j < m;j++) {
                if(t.charAt(i) == s.charAt(j)) {
                    cur[j + 1] = cur[j] + pre[j]; 
                }else {
                    cur[j + 1] = cur[j];
                }
            }
            pre = cur;
        }
        return pre[m];
    }
}
```

