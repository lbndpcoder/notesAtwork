[TOC]

# Sorting

## 1. Leetcode 179

Given a list of non negative integers, arrange them such that they form the largest number.

**Example 1:**

```
Input: [10,2]
Output: "210"
```

**Example 2:**

```
Input: [3,30,34,5,9]
Output: "9534330"
```

找到组合起来最大的数字：

- 首先将所有的数字变成 String ；
- 然后进行排序；
  - 因为如果一个 String 如果和每一个 String 的组合都相比其他组合成的数字最大，说明这个 String 一定是放在最前面的；
  - 所以如果一个 String 放在后面的时候比它放在前面的时候都要小，那么这个 String 一定是在前面的；

```java
class Solution {
    public String largestNumber(int[] nums) {
        int len = nums.length;
        List<String> l = new ArrayList<>();
        int i = 0;
        for(int num:nums) {
            l.add(Integer.toString(num));
        }
        Collections.sort(l,(a,b)->(int)(Long.parseLong(b + a) - Long.parseLong(a + b)));
        StringBuilder sb = new StringBuilder();
        for(String str:l) {
            sb.append(str);
        }
        if(sb.toString().charAt(0) == '0') return "0";
        return sb.toString();
    }
}
```



## 2. Leetcode 324

Given an unsorted array `nums`, reorder it such that `nums[0] < nums[1] > nums[2] < nums[3]...`.

**Example 1:**

```
Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].
```

**Example 2:**

```
Input: nums = [1, 3, 2, 2, 3, 1]
Output: One possible answer is [2, 3, 1, 3, 1, 2].
```

就是说将整个数组变成 nums[0] < nums[1] > nums[2] < nums[3]…这种的形式：

- 首先排序，找到中间的位置，也就是说中间的位置的右侧为较大的一侧，中间的左侧为较小的一侧；
- 首先将中间的位置放在结果数组的第一个位置，然后将最后一个数字（最大的）放在下一个，然后放中间的前一个，以此类推；

```java
class Solution {
    public void wiggleSort(int[] nums) {
        int len = nums.length;
        int[] copy = Arrays.copyOf(nums,len);
        Arrays.sort(copy);
        int m = (nums.length + 1) >> 1;
        int p = 0;
        for(int i = len - 1,j = m - 1;i > m - 1;i--,j--) {
            nums[p++] = copy[j];
            nums[p++] = copy[i];
        }
        if(p == len - 1) {
            nums[p] = copy[0];
        }
    }
}
```



# String

## 1. Leetcode 14

###solution 1 (Trie)

###solution 2 (String)