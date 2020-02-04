[TOC]

# 1. Leetcode 152

Given an integer array `nums`, find the contiguous subarray within an array (containing at least one number) which has the largest product.

**Example 1:**

```
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```

找到连续子数组中元素相乘最大的数值

- 需要比较的元素就是当前的元素或者是当前元素和之前的最大子数组乘积中的最大值或者之前子数组和当前的元素相乘得到的最小的数值。
- 要求的是最大值，但是最大值可能是从最小的负数乘一个负数得到的。

 ```java
class Solution {
    public int maxProduct(int[] nums) {
        int size = nums.length;
        if(size == 1) {
            return nums[0];
        }
        int max = nums[0];
        int min = nums[0];
        int res = nums[0];
        for(int i = 1;i < size;i++) {
            int tempMax = max;
            int tempMin = min;
            max = Math.max(nums[i],Math.max(nums[i]*tempMax,nums[i]*tempMin));
            min = Math.min(nums[i],Math.min(nums[i]*tempMin,nums[i]*tempMax));
            res = Math.max(res,max);
        }
        return res;
    }
}
 ```

# 2. Leetcode 746（DP）

On a staircase, the `i`-th step has some non-negative cost `cost[i]` assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

**Example 1:**

```
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
```

这道题的大概意思有几个主要的点：

- 1.可以从第一个或者第二个位置起跳，并且可以跳一个或者两个，跳到数组之外结束
- 2.落在的点的数值就是cost，要求整个的花费最少。

其实整个问题用DP的思想来解决的话可以这样理解，在当前的位置上，有两种方式可以跨越当前的位置

- 1.落在当前的位置。
- 2.在前一个位置跨越当前的位置。

如果是落在当前的位置那么可以知道的是经过上个位置的最佳的跳法无论怎么跳都得跳到当前的位置所以可以得到的是花费为
$$
min+cost[i]
$$
如果是跳跃当前的位置，那么需要必须经过当前位置的上一个位置，所以可以得到cost为：
$$
minPre + cost[i - 1]
$$
所以只需要在比较这两种跳法哪一个花费少就可以了：

```java
class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int min = 0;
        int minPre = 0;
        int size = cost.length;
        if(size == 0) {
            return 0;
        }
        if(size == 1) {
            return cost[0];
        }
        for(int i = 1;i < size;i++) {
            int temp = min;
            min = Math.min(minPre + cost[i - 1],min + cost[i]);
            minPre = temp;
        }
        return min;
    }
}
```

