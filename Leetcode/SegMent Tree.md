[TOC]

# SegMentTree

##leetcode 493 Reverse Pairs

Given an array `nums`, we call `(i, j)` an ***important reverse pair\*** if `i < j` and `nums[i] > 2*nums[j]`.

You need to return the number of important reverse pairs in the given array.

**Example1:**

```java
Input: [1,3,2,3,1]
Output: 2
```

​	从题目的描述的问题来看，就是要找到一个数组 $A \quad [a_1,a_2,a_3,...,a_n]$  如果其中的某一元素在前面并且它的数值大于出现在其后面的元素的二倍那么计数一次。例子中：$3 > 1 * 2$ ，并且有两个3存在所以输出为 2 。要解决这样一个问题首先可以利用一个暴力的方法，比较每一个当前的数值和后面的数值的大小关系然后计数，那么时间复杂度为 $O(n^2)$  。

​	因为存储的数字都是比较大的数字，可以思考构建一个如下图所示的树形结构将所有的数组中数字全部作为叶子节点存储的数字，而树形结构中的每一个内部的节点中都代表的是一个范围，这样做的目的就是当当前的数字 $2*a_j+1$ 如果小于等于某一个内部节点的所处范围的最小值，说明该节点范围内的所有出现过的所有数值都是满足条件的，此时可以不需要遍历每一个数值。相当于将每一个数组中的数字分别放入一个个大的范围和小的范围，这一个个范围分别由一个个内部节点代笔，并将此范围的大小存储在节点中。但是此方法的缺点在于需要将从最大的范围即$Integer.MIN\_VALUE-Integer.MAX \_ VALUE$ 作为初始的根节点的范围，根节点的左右节点代表的范围则是$Integer.MIN\_VALUE - 0$ 右孩子节点则为$1-Integer.MAX \_ VALUE$ 不断的划分将，直到一个确定的数值。当前的数字$2*a_j+1$如果大于当前的范围的最大值说明不存在满足条件的数字，如果数字处于中间，那么说明更小的范围找到满足条件的节点。因为在建立树的情况下整个树的高度为$log(MAX\_VALUE)$ 所以在计算的时候的时间复杂度为$o(nlog(MAX\_VALUE))$。 

<img src="/Users/liubonan/Pictures/SegMentTree.png" alt="SegMentTree" style="zoom:50%;" />

```java
class Solution {
    class Seg {
        public int count;
        public long min;
        public long max;
        Seg l,r;
        public Seg(long min, long max) {
            this.min = min;
            this.max = max;
            count = 0;
            l = null;
            r = null;
        }
        public void add(long n) {
            count++;
            if(min >= max) return;
            long mid = (max - min) / 2L + min;
            if(n <= mid) {
                if(l == null) this.l = new Seg(min, mid);
                l.add(n);
            }else {
                if(r == null) this.r = new Seg(mid + 1, max);
                r.add(n);
            }
        }
        public int co(long n) {
            if(n <= min) return count;
            if(n > max) return 0;
            return (l == null?0:l.co(n)) + (r == null?0:r.co(n));
        }
    }
    public int reversePairs(int[] nums) {
        int res = 0;
        Seg root = new Seg(Integer.MIN_VALUE, Integer.MAX_VALUE);
        for(int i = 1;i < nums.length;i++) {
            root.add(nums[i - 1]);
            res += root.co(nums[i] * 2L + 1L);
        }
        return res;
    }
}
```

上面的方法显然的缺点就是在建立一个树的时候不根据解决问题进行建树，树的固定深度为$log_2 MAX\_VALUE$ 这样的话可以进一步减少时间复杂度。如果利用给定的数组，不断的划分区间，在小范围内得到应该取得的数值，然后将小范围内的数字进行排序，比较小范围的数字和另一个小范围内的有序子数组。此时的时间复杂度为$O(Nlog_2N)$

```java
class Solution {
    public int count = 0;
    public int reversePairs(int[] nums) {
        mergeSort(nums, Arrays.copyOf(nums, nums.length), 0, nums.length - 1);
        return count;
    }
    
    public void mergeSort(int[]nums, int[] buff, int low, int high) {
        if(low >= high) return;
        int mid = (low + high) / 2;
        mergeSort(buff, nums, low, mid);
        mergeSort(buff, nums, mid + 1, high);
        int left = low;
        int right = mid + 1;
        while(left <= mid && right <= high) {
            if(buff[left] > 2L * buff[right]) {
                count += mid - left + 1;
                right++;
            }else {
                left++;
            }
        }
        merge(nums, buff, low, high);
    }
    public void merge(int[] nums, int[] buff, int low, int high) {
        int i = low;
        int left = low;
        int mid = (low + high) / 2;
        int right = mid + 1;
        while(left <= mid && right <= high) {
            if(buff[left] < buff[right]) {
                nums[i++] = buff[left++];
            }else {
                nums[i++] = buff[right++];
            }
        }
        while(left <= mid) nums[i++] = buff[left++];
        while(right <= high) nums[i++] = buff[right++];
    }
}
```

