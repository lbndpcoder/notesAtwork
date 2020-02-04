[TOC]

# 1. Leetcode 56

Given a collection of intervals, merge all overlapping intervals.

**Example 1:**

```
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
```

**Example 2:**

```
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

这道题的意思就是取并集：【1，3】【2，6】—>【1，6】，所以思路很简单就是遍历一遍整体的输入，判断如果当前的可以合并就进行合并；

- 首先在构造数据结构的时候利用可以自动排序的 TreeMap ，并且在构造的时候如果 start 的数值一样只保存较大的 end 数值；
- 遍历所有的排序后的 key（也就是start数值），如果当前的 key 大于lastKeyValue就说明两个不在一个区间；
  - lastKeyValue会不断的更新，如果当前的 value 大于上一个的value，说明右侧的边界发生变化；
  - 如果不在一个区间，将之前的区间加入并更新当前的start，并且更新 lastKeyValue；

```java
class Solution {
    public List<Interval> merge(List<Interval> intervals) {
        TreeMap<Integer,Integer> tm = new TreeMap<>();
        for(Interval a:intervals) {
            if(tm.containsKey(a.start)) {
                tm.put(a.start,Math.max(tm.get(a.start),a.end));
            }else {
                tm.put(a.start,a.end);
            }
        }
        int lock = 0;
        int lastKeyValue = 0;
        int start = 0;
        List<Interval> res = new ArrayList<>();
        if(intervals.size() == 0) {
            return res;
        }
        for(int s:tm.keySet()) {
            if(lock == 0) {
                start = s;
                lastKeyValue = tm.get(s);
            }
            if(s <= lastKeyValue) {
                lock = 1;
                lastKeyValue = Math.max(tm.get(s),lastKeyValue);
                continue;
            }else {
                res.add(new Interval(start,lastKeyValue));
                start = s;
                lastKeyValue = tm.get(s);
            }
        }
        res.add(new Interval(start,lastKeyValue));
        return res;
    }
}
```

在代码中的 lock 是第一个数值在第一次加入的时候需要的，并且整个循环结束，最后一次遍历的结果不会在循环中加入res中，所以需要再次加入一次；

# 2. Leetcode 209（Two pointers）

Given an array of **n** positive integers and a positive integer **s**, find the minimal length of a **contiguous** subarray of which the sum ≥ **s**. If there isn't one, return 0 instead.

**Example:** 

```
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
```

找到加和大于等于 s 的最小长度，利用双指针：

- 其中一个指针 j 找到加和大于等于 s 的右侧边界，之后不断减去 i 的位置的数值直到小于 s；
  - 不断的更新整个长度；

```java
class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        int i = 0;int j = 0;
        int sum = 0;
        int res = Integer.MAX_VALUE;
        while(j < nums.length) {
            sum += nums[j++];
            while(sum >= s) {
                res = Math.min(res,j - i);
                sum -= nums[i++];
            }
        }
        return res == Integer.MAX_VALUE?0:res;
    }
}
```

