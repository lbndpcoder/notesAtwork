[TOC]

# 1. Leetcode 769（划分块）

Given an array `arr` that is a permutation of `[0, 1, ..., arr.length - 1]`, we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?

**Example 1:**

```
Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
```

目的是找到最几个划分区域然后在划分区域将数组重新排列之后整体的数组就能有序；

- 因为如果数组是长度n的，那么说明给定的数字是从 0 到 n-1 的；
- 如果一段数字需要重新排序并且可以保证只在当前的数组块中排序就可以说明：
  - 当前的数字是出现过的最大的；
  - 当前的数字的大小=它处在的位置；（排序后idnex（n）= n）

```java
class Solution {
    public int maxChunksToSorted(int[] arr) {
        int size = arr.length;
        int max = 0;
        int count = 0;
        for(int i = 0;i < size;i++) {
            max = Math.max(max,arr[i]);
            if(max == i) {
                 count++;
            }
        }
        return count;
    }
}
```

# 2. Leetcode 768（划分块）

*This question is the same as "Max Chunks to Make Sorted" except the integers of the given array are not necessarily distinct, the input array could be up to length 2000, and the elements could be up to 10**8.*

和上面的题是一样的，只是在这里给定的数组可以有重复数字的：

- 从左到右构建一个 maxLeft 数组，其中的每一个元素可以代表的是这个数字的辐射范围，也就是在排序后的这块儿区域{0到当前位置 i }最大的数值是一个数字 maxLeft[ i ];
- 从右到左构建 minRight 数组，代表的是在每一个区域内的最小数值；
- 在比较的时候，如果出现当前的最大数值小于或者等于下一个的最小数值那么说明这两个数字不在一个划分区域里面，所以划分；
  - 在划分的时候，至少有一次划分count = 1；

```java
class Solution {
    public int maxChunksToSorted(int[] arr) {
        int size = arr.length;
        int[] maxLeft = new int[size];
        int[] minRight= new int[size];
        maxLeft[0] = arr[0];
        minRight[size - 1] = arr[size - 1];
        for(int i = 1;i < size;i++) {
            maxLeft[i] = Math.max(maxLeft[i - 1],arr[i]);
        }
        for(int i = size - 2;i >= 0;i--) {
            minRight[i] = Math.min(minRight[i + 1],arr[i]);
        }
        int count = 1;
        for(int i = 0;i < size - 1;i++) {
            if(maxLeft[i] <= minRight[i + 1]) {
                count++;
            }
        }
        return count;
    }
}
```

这个解法其实是通用的也可以解决上面的题；

# 3. Leetcode 274（桶排序）

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the [definition of h-index on Wikipedia](https://en.wikipedia.org/wiki/H-index): "A scientist has index *h* if *h* of his/her *N* papers have **at least** *h*citations each, and the other *N − h* papers have **no more than** *h* citations each."

**Example:**

```
Input: citations = [3,0,6,1,5]
Output: 3 
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
             received 3, 0, 6, 1, 5 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
```

这道题的意思给定一个人的发表的论文的影响因子来找到这个人的 H-index：

- 这个人的 h-index 假如是3那么影响力大于等于3的文章数必须大于等于3篇文章，也就是说发表文章的数量决定了这个人h-index的最高数值发5篇文章h-index最高只可能是5；

根据题意制定策略：

- 将不同的影响因子的文章分别存储数量；
- 因为文章的数量制约了 h-index 所以最高的 h-index 只可能是文章的数量，所以大于等于这个值的文章都放在这个等级内来决定是否是这个等级，其他的小于这个等级的文章分别存放数量；
- 由于是要找最大的等级，所以从整个**等级分组**从最高的等级开始计数，如果此时的文章数量大于等于此时的等级那么这个等级就是最后的等级；

```java
class Solution {
    public int hIndex(int[] citations) {
        int size = citations.length;
        int[] h = new int[size + 1];
        for(int i = 0;i < size;i++) {
            if(citations[i] >= size) {
                h[size] += 1;
            }else {
                h[citations[i]] += 1;
            }
        }
        int count = 0;
        int res = 0;
        for(int i = size;i >= 0;i--) {
            count += h[i];
            if(count >= i) {
                res = i;
                break;
            }
        }
        return res;
    }
}
```

#4. Leetcode 275（binary search）

和上面的题一样只是这次给的是一个有序的数组，解决的办法用上面的办法也可以解决，下面说一个二分查找的解决方案：

- 在整个数组中查找一个位置，这个位置和尾部的距离（就是大于这个h-index的文章的个数）要大于或者等于这个位置的论文的 h 值；
  - 设定一个 left / right，二分查找 mid 数值；
  - 如果距离小于当前的引用数值说明需要在左侧找到合适的点；
  - 要是大于的话说明可能有更大的；
  - 最终的时候 left > right 的情况下，说明要不是不够，要不是大一个位置，因为left的位置是绝对"安全的”；

```java
class Solution {
    public int hIndex(int[] citations) {
        int size = citations.length;
        int left = 0;
        int right = size - 1;
        int mid = 0;
        while(left <= right) {
            mid = (left + right) >> 1;
            if(citations[mid] == size - mid) return citations[mid];
            else if(size - mid < citations[mid]) {
            right = mid - 1;
            }else {
                left = mid + 1;
            }
        }
        return size - right - 1;
    }
}
```

还有一个比较容易思考的方法：

顺着找，找到了大于这个文章引用的个数>= 这个文章的H值继续找，知道 <= 了再停止；

```java
class Solution {
    public int hIndex(int[] citations) {
        int size = citations.length;
        int res = 0;
        for(int i = 0;i < size;i++) {
            if(size - i <= citations[i]) {
                res = size - i;
                break;
            }
        }
        return res;
    }
}
```

