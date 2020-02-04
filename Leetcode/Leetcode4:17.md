[TOC]

# 1. Leetcode 4

There are two sorted arrays **nums1** and **nums2** of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume **nums1** and **nums2** cannot be both empty.

**Example 1:**

```
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
```

**Example 2:**

```
nums1 = [1, 2]
nums2 = [3, 4]
```

这个题的意思就是从两个有戏的递增的数组中找到中位数，其实有很多做法但是作为一个**hard**要要有敬畏之心鸭。。。O(log (m+n))思路如下：

- 首先要知道假设组成最终的数组的一半需要多少个数字：
  - (Len1 + len2 + 1) / 2;
  - 偶数的话就是一半的个数；奇数的话是包括中位数的左侧的数字个数；
- 现在不断的将将 nums1 数组（长度较小的那个数组）中的一些数字放入组合在一起的数组当中，如果nums1中放入的数字中最大的那个还小于nums2放入组合在一起的数组的最后一个数字，继续寻找看看nums1是不是能找到nums1中的一个数字大于 nums2 放入最终数组左半区的最大的那个，最终找到的是nums1放入左半区的数字的个数；
- 此时判断nums1放入左半区的最大的那个数字和nums2放入左半区的最大的那个数字竞争谁更大才能放在中间的那个位置，因为这两个数字都是放在左半区的；

```java
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int l1 = nums1.length;
        int l2 = nums2.length;
        if(l1 > l2) return findMedianSortedArrays(nums2,nums1);
        int l = 0;int r = l1;
        int k = (l1 + l2 + 1) / 2;
        while(l < r) {
            int mid = l + (r - l) / 2;
            if(nums1[mid] < nums2[k - mid - 1]) {
                l = mid + 1;
            }else {
                r = mid;
            }
        }
        int m1 = l;
        int m2 = k - l;
        int res1 = Math.max(m1 <= 0?Integer.MIN_VALUE:nums1[m1 - 1],m2 <= 0?Integer.MIN_VALUE:nums2[m2 - 1]);
        if((l1 + l2) % 2 != 0) return res1;
        int res2 = Math.min(m1 >= l1?Integer.MAX_VALUE:nums1[m1],m2 >= l2?Integer.MAX_VALUE:nums2[m2]);
        return (res1 + res2) / 2.0;
    }
}
```

# 2. Leetcode 189

Given an array, rotate the array to the right by *k* steps, where *k* is non-negative.

**Example 1:**

```
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```

**Example 2:**

```
Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```

将后面的数字向前移：
$$
总长度 - 移动的长度 + 1 - 1
$$
这样就计算的到了新开始的数组的下标了，但是移动的长度可能会很多次，所以对数组进行求余操作，这个System.arraycopy：

- 第一个参数是被复制的数组，第二个参数是开始复制的下标；
- 第三个参数是复制的数组，第四个参数是复制到数组的下标，第五个参数是复制数组的长度；

```java
class Solution {
    public void rotate(int[] nums, int k) {
        int size = nums.length;
        int[] nums2 = new int[2 * size];
        System.arraycopy(nums,0,nums2,0,size);
        System.arraycopy(nums,0,nums2,size,size);
        int j = 0;
        if(k != 0) {
            for(int i = size - k % size;i < 2 * size - k % size;i++) {
                nums[j] = nums2[i];
                j++;
            }
        }
    }
}
```

# 3. Leetcode 33

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]`).

You are given a target value to search. If found in the array return its index, otherwise return `-1`.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of *O*(log *n*).

**Example 1:**

```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

**Example 2:**

```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

在旋转过的数组中找到taget数字：

- 首先找到旋转的部分在哪里；
- 根据旋转点求出真正的中间位置，就是恢复成原来状态下的数组的中间位置在现在数组的位置；

```java
class Solution {
    public int search(int[] nums, int target) {
        int len = nums.length;
        int l = 0;int r = len - 1;
        while(l < r) {
            int mid = l + (r - l) / 2;
            if(nums[mid] <= nums[r]) {
                r = mid;
            }else {
                l = mid + 1;
            }
        }
        int minIndex = l;l = 0;r = len - 1;
        while(l <= r) {
            int mid = l + (r - l) / 2;
            int realMid = (minIndex + mid) % len;
            if(nums[realMid] == target) return realMid;
            if(nums[realMid] < target) {
                l = mid + 1;
            }else {
                r = mid - 1;
            }
        }
        return -1;
    }
}
```



# 4. Leetcode 153

找到旋转数组之中的最小的数字，就是33的前一部分找到旋转的数字的位置：

- 找到中间位置的数字；
  - 如果小于或等于最右的数字那么说明这个中间的位置是在旋转前的前半部分的，可能是旋转的部分；
  - 如果大于那么说明是旋转位置的右侧，所以寻找的范围应该在mid的右侧，l = mid + 1； 

```java
class Solution {
    public int findMin(int[] nums) {
        int n = nums.length;
        int l = 0;int r = n - 1;
        while(l < r) {
            int mid = (l + r) / 2;
            if(nums[mid] > nums[r]) {
                l = mid + 1;
            }else {
                r = mid;
            }
        }
        return nums[l];
    }
}
```



# 5. Leetcode  81

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., `[0,0,1,2,2,5,6]` might become `[2,5,6,0,0,1,2]`).

You are given a target value to search. If found in the array return `true`, otherwise return `false`.

**Example 1:**

```
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
```

**Example 2:**

```
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
```

同样是在带有旋转的数组中搜索target，其中具有的是重复的元素，整体的情况分为三个情况：

- 当数组的mid在旋转点的左侧：target有三种位置；
  - target位于mid的左侧；
  - target位于mid的右侧但是在旋转点的左侧；
  - target位于mid的右侧位于旋转点的右侧；
- 当数组的mid在旋转点的右侧：target有三种位置；
  - target位于mid的右侧；
  - target位于mid的左侧但是在旋转点的右侧；
  - target位于mid的左侧位于旋转点的左侧；
- 当mid和最左最右都相等的时候此时只需要移动一侧就可以；

```java
class Solution {
    public boolean search(int[] nums, int target) {
        int len = nums.length;
        int l = 0;int r = len - 1;
        while(l <= r) {
            int mid = l + (r - l) / 2;
            if(nums[mid] == target) return true;
            if(nums[mid] < nums[r] || nums[mid] < nums[l]) {
                if(target <= nums[r] && nums[mid] < target) {
                    l = mid + 1;
                }else {
                    r = mid - 1;
                }
            }else if(nums[mid] > nums[r] || nums[mid] > nums[l]) {
                if(target >= nums[l] && nums[mid] > target) {
                    r = mid - 1;
                }else {
                    l = mid + 1;
                }
            }else {
                r--;
            }
        }
        return false;
    }
}
```

# SUMMARY

都是和旋转数组相关的题；

- 找到旋转点；
- 找到目标target在数组的位置；