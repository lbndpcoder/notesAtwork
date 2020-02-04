[TOC]

#题型：Combination Sum

这些题目都是关于在给定的数组中找到目标为target的组合或者组合数，大多数的题递归都可以解决，剩下的一部分题可以依靠DP的思路来解决。

## 1. Leetcode 39 \< Combination Sum I >

Given a **set** of candidate numbers (`candidates`) **(without duplicates)** and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sums to `target`.

The **same** repeated number may be chosen from `candidates` unlimited number of times.

**Note:**

- All numbers (including `target`) will be positive integers.
- The solution set must not contain duplicate combinations.

**Example 1:**

```
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
```

这道题是这一类型的最简单的一个问题，要解决的问题是在给定的数组中找到所有的组合方式，并且数组中的数字可以重复。简单的思路就是递归解决：

```java
class Solution {
    public List<List<Integer>> res = new ArrayList<>();
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        int size = candidates.length;
        List<Integer> a = new ArrayList<>();
        helper(candidates,target,a,0);
        return res;
    }
    public void helper(int[] candidates,int target,List a,int start) {
        if(target == 0) {
            res.add(new ArrayList<>(a));
            return;
        }
        if(target < 0) {
            return;
        }
        for(int i = start;i < candidates.length;i++) {
            a.add(candidates[i]);
            target -= candidates[i];
            helper(candidates,target,a,i);
            target += candidates[i];
            a.remove(a.size() - 1);
        }
    }
}
```

## 2. Leetcode 40 \< Combination Sum II >

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sums to `target`.

Each number in `candidates` may only be used **once** in the combination.

**Note:**

- All numbers (including `target`) will be positive integers.
- The solution set must not contain duplicate combinations.

**Example 1:**

```
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
```

这个题在上面的题的基础上增加了一个限制，就是不能利用重复的数字，并且重复的组合也不能出现，主要的方法还是递归，而改进就是，如果在当前层的前后的两个元素相同那么说明这两个计算一定会产生重复；并且在数组计算前要进行排序；

```java
class Solution {
    public List<List<Integer>> res = new ArrayList<>();
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        int len = candidates.length;
        Arrays.sort(candidates);
        List<Integer> a = new ArrayList<>();
        helper(candidates,target,0,a);
        return res;
    }
    public void helper(int[] nums,int target,int start,List<Integer> a) {
        if(target < 0) {
            return;
        }
        if(target == 0) {
            res.add(new ArrayList<>(a));
        }else {
            for(int i = start;i < nums.length;i++) {
                if(i > start && nums[i] == nums[i - 1]) {
                    continue;
                }
                a.add(nums[i]);
                target -= nums[i];
                helper(nums,target,i + 1,a);
                target += nums[i];
                a.remove(a.size() - 1);
            }
        }
    }
}
```

## 3. Leetcode 216\< Combination Sum III >

Find all possible combinations of ***k*** numbers that add up to a number ***n***, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:**

- All numbers will be positive integers.
- The solution set must not contain duplicate combinations.

**Example 1:**

```
Input: k = 3, n = 7
Output: [[1,2,4]]
```

**Example 2:**

```
Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
```

和前面的题的思路基本上是相同的，只是数组的给定的1-9的数字，判断的条件只需要判断两个，分别是当前的数字个数等于给定的要求的数字个数和目标和相同；

```java
class Solution {
    public List<List<Integer>> res = new ArrayList<>();
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<Integer> a = new ArrayList<>();
        helper(k,n,1,a);
        return res;
    }
    public void helper(int k,int n,int s,List<Integer> a) {
        if(n == 0 && k == 0) {
            res.add(new ArrayList<>(a));
            return;
        }else if(k < 0 || n < 0) {
            return;
        }
        for(int i = s;i <= 9;i++) {
            k -= 1;
            n -= i;
            a.add(i);
            helper(k,n,i+1,a);
            k += 1;
            n += i;
            a.remove(a.size() - 1);
        }
    }
}
```

##4. Leetcode 377\< Combination Sum IV>

Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

**Example:**

```
nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
```

如果想要求**组合的个数**的话就可以利用 **DP** 的思想来解决问题，这是一个很常见的思路：

- 构建一个长度为 （target + 1） 的数组；
  - 数组中的每一个元素都代表着利用给定数组组成这个数值的组合数；
- 每一次分别在一个数值部分遍历整个给定数组，从中"取出”数字用来组成该元素；
  - 如果大于0，那么在减去这个数值之后剩下的数值由给定数组的组合数 + 当前的组合数；

```java
class Solution {
    public int combinationSum4(int[] nums, int target) {
        int len = nums.length;
        int[] pattern = new int[target + 1];
        pattern[0] = 1;
        for(int i = 1;i <= target;i++) {
            for(int j = 0;j < len;j++) {
                if(i - nums[j] >= 0) {
                    pattern[i] += pattern[i - nums[j]];
                }
            }
        }
        return pattern[target];
    }
}
```

##5. Leetcode 494\< Combination Sum V >

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols `+` and `-`. For each integer, you should choose one from `+`and `-` as its new symbol.Find out how many ways to assign symbols to make sum of integers equal to target S. 

**Example 1:**

```
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
```

这个题的递归解法其实和 Combination Sum 没有什么关系，但是其中的一种解法就是**Combination Sum**的思路，只是更加复杂：

- 这里是不带重复数值；

可以重复数值：

- 遍历的时候多次遍历给定的数组，每一次确定一个pattern中组成一个数值的个数；

不可以重复数值：

- 从后往前多次遍历pattern，每一次从给定数组中取出一个数字；

先说说整体的思路是什么，首先对问题要进行一个转化，本题的原来的题的意思是对整个数组添加正负号，使得结果为 S ，其实可以这么理解，将所有添加正号的数字当作 N ，所有的添加负号的数字的和当作 M ，所有的数字的求和为sum，那么有：
$$
N-M = taget\\
N+M = sum \\
N = (S + sum) / 2
$$
所以说要存在这样的正负组合，其中要有 N 为偶数，并且问题转化成了在给定数组中找到和为 N 的个数，并且不能重复；

```java
class Solution {
    public int findTargetSumWays(int[] nums, int S) {
        int sum = 0;
        for(int num:nums) {
            sum += num;
        }
        int s = (S + sum) / 2;
        return S > sum || (S + sum) % 2 != 0?0:find(nums,s);
    }
    public int find(int[] nums,int s) {
        int len = nums.length;
        int[] pattern = new int[s + 1];
        pattern[0] = 1;
        for(int num:nums) {
            for(int j = s;j >= 0;j--) {
                if(j - num >= 0) {
                    pattern[j] += pattern[j - num];
                }
            }
        }
        return pattern[s];
    }
}
```

