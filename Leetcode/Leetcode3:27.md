[TOC]

# 1. Leetcode 128 （union）

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(*n*) complexity.

**Example:**

```
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

找到连续子串的长度，其实解决方法很多，但是要保证在O（n）下解决还是要有新思路的：

- 利用的是 HashMap
  - 存储每一个出现的数值作为 Key，其中的对应的 value 是这个 Key 对应的连续子串的长度；
- 出现一个新的元素，判断和他相邻的元素是否出现在map中；
  - 如果出现就将两边的元素所在连续子串的长度（value）之和加 1 作为这个新出现的元素的所在子串的长度；
  - 并且更新距离当前元素一定距离的位置的数值，这个距离是相邻的元素的所在子串的长度，就是说更新的是我们当前的元素所在子串的**头部**和**尾部**位置上的value；

```java
class Solution {
    public int longestConsecutive(int[] nums) {
        HashMap<Integer,Integer> m = new HashMap<>();
        int size = nums.length;
        int max = 0;
        for(int i = 0;i < size;i++) {
            if(!m.containsKey(nums[i])) {
                int left = m.containsKey(nums[i] - 1)?m.get(nums[i] - 1):0;
                int right = m.containsKey(nums[i] + 1)?m.get(nums[i] + 1):0;
                int sum = left + right + 1;
                m.put(nums[i],sum);
                if(sum > max) {
                    max = sum;
                }
                m.put(nums[i] - left,sum);
                m.put(nums[i] + right,sum);
            }else {
                continue;
            }
        }
        return max;
    }
}
```

# 2. Leetcode 198（DP）

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight **without alerting the police**.

给定一个数组不能连续选择其中的数字要使得其中的和最大；

- 主要需要比较的是在上一个元素的位置之前的最大值 max ；
- 在上上个元素位置之前的最大值 last + nums[i] ;

```java
class Solution {
    public int rob(int[] nums) {
        int size = nums.length;
        if(size < 1) {
            return 0;
        }
        if(size == 2) {
            return Math.max(nums[0],nums[1]);
        }
        int max = 0;
        int last = 0;
        for(int i = 0;i < size;i++) {
            int temp = max;
            max = Math.max(nums[i] + last,max);
            last = temp;
        }
        return max;
    }
}
```

# 3. Leetcode 300（*）

Given an unsorted array of integers, find the length of longest increasing subsequence.

**Example:**

```
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
```

找到最长的递增子串：

- 用二分查找找到插入的位置，按递增顺序插入到合适的位置；
  - [1,2,5]插入4，那么5就被替换掉了变成[1,2,4]；
  - 如果插入的是大于5的数字比如7，那么就变成[1,2,5,7];
- 最后得到的序列的长度就是最长的递增子串；

```java
class Solution {
    public int lengthOfLIS(int[] nums) {
        int size = nums.length;
        int[] dp = new int[size];
        Arrays.fill(dp,Integer.MAX_VALUE);
        int len = 0;
        for(int a:nums) {
            int i = bs(dp,len,a);
            dp[i] = a;
            if(i == len) {
                len++;
            }
        }
        return len;
    }
    public int bs(int[] nums,int high,int target) {
        int low = 0;
        while(low <= high) {
            int mid = low + (high - low) / 2;
            if(nums[mid] == target) {
                return mid;
            }else if(nums[mid] < target) {
                low = mid + 1;
            }else {
                high = mid - 1;
            }
        }
        return low;
    }
}
```

# 4. Leetcode 215 （同703）

Find the **k**th largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

**Example 1:**

```
Input: [3,2,1,5,6,4] and k = 2
Output: 5
```

## 思路（1）优先队列

优先队列队列的头部是最小的元素：

- 如果来的元素小于头顶的元素那么新来的元素在队列的顶部；
- 如果来的元素大于队列的顶端元素，那么队列的顶端元素不是第 k 个最大的元素；

```java
class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int i = 0;i < nums.length;i++) {
            pq.offer(nums[i]);
            while(pq.size() > k) {
                pq.poll();
            }
        }
        return pq.peek();
    }
}
```

##思路（2）分治/快排

第二种思路是利用快速排序的思路：

- 每一次进行快排（从小到大）中间元素将整个数列分割成为 left / right，中间点的位置为mid
  - 如果 right 的元素个数大于 k，说明第 k 大的元素就在右侧继续递归；
  - 如果 left 的元素 大于 k，说明第 k 大元素是 左侧的第 k - (high - mid + 1)大的元素；
  - 如果mid = k 说明位置 mid 的元素就是要找的元素；

```java
class Solution {
    public int findKthLargest(int[] nums, int k) {
        return helper(nums,0,nums.length - 1,k);
    }
    
    public int quickSortOnce(int[] nums,int low,int high) {
        int p = low - 1;
        int basic = nums[high];
        for(int i = low;i <= high;i++) {
            if(nums[i] < basic) {
                p++;
                int temp = nums[p];
                nums[p] = nums[i];
                nums[i] = temp;
            }
        }
        int temp = nums[p + 1];
        nums[p + 1] = nums[high];
        nums[high] = temp;
        return p + 1;
    }
    public int helper(int[] nums,int low,int high,int target) {
        int mid = quickSortOnce(nums,low,high);
        if((high - mid  + 1) == target) {
            return nums[mid];
        }else if((high - mid + 1) > target) {
            return helper(nums,mid + 1,high,target);
        }else {
            return helper(nums,low,mid - 1,target - high + mid - 1);
        }
    }
}
```

