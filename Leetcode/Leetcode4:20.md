[TOC]

# 1.Leetcode 154

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  `[0,1,2,4,5,6,7]` might become  `[4,5,6,7,0,1,2]`).

Find the minimum element.

The array may contain duplicates.

**Example 1:**

```
Input: [1,3,5]
Output: 1
```

**Example 2:**

```
Input: [2,2,2,0,1]
Output: 0
```

这个题和之前的在旋转数组（带有重复数值）中找到一个 targte 数值的题是一样的思路：一共有这样几种情况：

- mid < r  —> 此时说明我们要寻找的旋转点在左侧；
  - 而只有在mid 小于 r 并且 mid==l 的情况下说明 l 的位置是要寻找的最小值（旋转点）；
- mid > l —> 此时说明我们要寻找的旋转点在右侧；
  - 因为 r 的位置始终处在数值较小的区域，所以当mid > l 并且 mid == r的情况下我们能知道旋转点就是l所处的位置；

```java
class Solution {
    public int findMin(int[] nums) {
        int l = 0;
        int r = nums.length - 1;
        while(l < r) {
            int mid = l + (r - l) / 2;
            if(nums[mid] < nums[r] || nums[mid] < nums[l]) {
                if(nums[mid] == nums[l]) {
                    return nums[l];
                }else {
                    r = mid;
                }
            }else if(nums[mid] > nums[r] || nums[mid] > nums[l]){
                if(nums[mid] == nums[r]) {
                    return nums[l];
                }else {
                    l = mid + 1;
                }
            }else {
                r -= 1;
            }
        }
        return nums[r];
    }
}
```



# 2. Leetcode 410

