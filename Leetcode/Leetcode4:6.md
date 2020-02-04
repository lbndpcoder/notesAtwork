[TOC]

# 1. Leetcode 526（递归搜索）

Suppose you have **N** integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these **N** numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

1. The number at the ith position is divisible by **i**.
2. **i** is divisible by the number at the ith position.

Now given N, how many beautiful arrangements can you construct?

**Example 1:**

```
Input: 2
Output: 2
Explanation: 

The first beautiful arrangement is [1, 2]:

Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

The second beautiful arrangement is [2, 1]:

Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
```

一个数组 nums 中的所有的元素在每一个 **i** 位置：

- 如果nums[i] % i == 0 或者 i % nums[i] == 0;

那么就说这个是一个完美的"安排”；输入的是一个数字N，那么这个数组元素就是从 1 到 N 的 N 个数字，找到所有的安排个数；

这道题的思路是递归查找，主要的部分在于要把已经利用过数字去除掉也就是判重复：

- 在每一层要遍历所有的数字找到该位置上满足条件的数字，然后递归进入下一层；
  - 在每一层的下标是不变的，变化的是nums[i]，要遍历的是整个数组从该位置开始的所有数值，找到满足条件的点；
  - 为了避免重复，所以在每一层开始进行交换，将要进行判断是否满足条件的点进行交换，这样利用过的点在后面下一层中不会被遍历到；

```java
class Solution {
    public int count = 0;
    public int countArrangement(int N) {
        int[] nums = new int[N+1];
        for(int i = 0;i <= N;i++) {
            nums[i] = i;
        }
        helper(nums,N);
        return count;
        
    }
    public void helper(int[] nums,int start) {
        if(start == 0) {
            count++;
            return;
        }
        for(int i = start;i > 0;i--) {
            swap(nums,i,start);
            if(nums[start] % start == 0 || start % nums[start] == 0) {
                helper(nums,start - 1);
            }
            swap(nums,start,i);
        }
    }
    public void swap(int[] nums,int i ,int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
```

# 2. Leetcode 667（规律）

Given two integers `n` and `k`, you need to construct a list which contains `n` different positive integers ranging from `1`to `n` and obeys the following requirement: 
Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly `k` distinct integers.

If there are multiple answers, print any of them.

**Example 1:**

```
Input: n = 3, k = 1
Output: [1, 2, 3]
Explanation: The [1, 2, 3] has three different positive integers ranging from 1 to 3, and the [1, 1] has exactly 1 distinct integer: 1.
```

也是给定一定的规则找到合适的序列满足规则，这个题的规则就是给定n，k两个数；

- n 代表的是数字是从1到n的；
- k代表的是前后两个数字的绝对值的差的个数为 k 个，这个差应该是不同的数字；

其实问题可以这样想：

[1,2,3,4,5,6,7] —> [7,1,6,2,5,3,4] 这是整个数组可以得到的最大的差的个数；就是分别从右侧找到一个数值，左侧找到一个数值，分别加入到结果数组中就组成了结果的数组；如果给定的是 k 个不同的差就只需要判断停止的条件，并且后面的数字按顺序排列就可以，比如如果 k=3 —>[7,1,6,5,4,3,2]

- 分别设定一个右侧的指针 right ，左侧的指针 left ：
  - 每一次首先将右侧指针的数字放入结果数组，此时代表已经至少有一个不同的差了就是"1"；并且需要左右的交替执行，设置f参数；
  - 同理，left也是，如果每一次放入一个数值都代表着不同的差值增加1，count++；
- 设置count < k的时候依次放入，当足够的时候，要记录的是最后出现的数值：
  - 如果这个数值大于中间的数值 mid = n >> 1;说明后面的数字都应该是递减的保持1的差值；如果是小于等于的话，后面的数值就应该是递增的；

```java
class Solution {
    public int[] constructArray(int n, int k) {
        int[] res = new int[n];
        int left = 1;
        int right = n;
        int f = 0;
        int count = 0;
        int pos = 0;
        int lr = right;
        int mid = n >> 1;
        int temp = right;
        while(pos < n) {
            if(count < k) {
                if(f == 0) {
                    lr = right;
                    res[pos++] = (right--);
                    f = (f+1) % 2;
                    count++;
                }else {
                    lr = left;
                    res[pos++] = (left++);
                    f = (f + 1) % 2;
                    count++;
                }
                temp = lr;
            }else {
                if(lr <= mid) {
                    res[pos++] = (++temp);
                }else {
                    res[pos++] = (--temp);
                }
            }
        }
        return res;
    }
}
```



