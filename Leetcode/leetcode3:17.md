[TOC]

# 1. Leetcode 70 

You are climbing a stair case. It takes *n* steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

**Note:** Given *n* will be a positive integer.

**Example 1:**

```
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

这道题要和746题相对应，在746主要是要求一个最小的花费，本题的思路主要是找到所有的跳法。

- 当前的位置作为最后一个位置的话，主要有两种方式跃过这个位置。第一种就是从这个位置起跳达到结尾，第二种就是从上一个位置起跳越过这个位置。
- 在第一种情况下，得到的跳跃方式是基于上一个位置作为结束的跳跃方式的数量的。
- 第二种情况是基于上上一个位置作为结束的跳跃方式的。

```java
class Solution {
    public int climbStairs(int n) {
        int step = 1;//可以理解为第一个位置只有一种跳法就是直接跳
        int stepPre = 0;
        for(int i = 0;i < n;i++) {
            int temp = step;
            step = step + stepPre;
            stepPre = temp;
        }
        return step;
    }
}
```

# 2. Leetcode 53

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

**Example:**

```
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

这道题的意思就是找到加和最大的子串，这道题是乘积为最大值的子串的简化版。主要需要两个关键点：

- 首先存储的是求得的最大值中的最大数值res作为结果。
- 在每一次新到来的数字，只需要比较加上这个数字是不是比这个数字大，如果加上变小了的话就从这个数字开始作为一个新的子串的开端。

```java
class Solution {
    public int maxSubArray(int[] nums) {
        int m = nums[0];
        int size = nums.length;
        if(size < 1) {
            return 0;
        }
        int res = nums[0];
        for(int i = 1;i < size;i++) {
            m = Math.max(nums[i],nums[i] + m);
            res = Math.max(m,res);
        }
        return res;
    }
}
```

# 3. Leetcode 713 (two pointers)

Your are given an array of positive integers `nums`.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than `k`.

**Example 1:**

```
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
```

这道题的意思就是说找到所有子串的乘机小于k的个数，**允许重复的子串**：

- 设定两个指针 i 和 j分别表示满足条件的子串的start和end
- 用 j 每一次向后移动，如果当前的乘积大于 k 的话将 i 向前移动找到使得乘积满足小于k的位置。
- 因为是子串的乘积数值，所以每次得到的满足条件的子串的的子串中肯定是满足条件的并且其中的子串数量为

$$
j - i + 1
$$

- 每次得到一个子串并加上满足条件的子串的子串的数量。

```java
class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        int size = nums.length;
        int product = 1;
        int count = 0;
        for(int i = 0,j = 0;j < size;j++) {
            product *= nums[j];
            while(i <= j && product >= k) {
                product /= nums[i];
                i++;
            }
            count += (j- i + 1);
        }
        return count; 
    }
}
```

# 4. 字节跳动2019笔试（2）

题目是要对字符串进行纠错，主要纠错的标准如下：

- AAA如果出现三个连续的那么就删掉最后一个变为AA。
- AABB如果这种情况就变为AAB。
- AABBCC这种仍然更改第二个变为AABCC。

针对这个题进行解决的方式是一一判断：

- 设定一个空的字符串，逐渐添加原字符串中的元素。
- 当出现AA/A的情况不添加。
- 当出现AAB/B的情况不添加。

```java
public class ByteDanceTwo {
    public String correct(String str) {
        StringBuffer sb = new StringBuffer();
        int size = str.length();
        for(int i = 0;i < size;i++) {
            if(!aaA(sb,str.charAt(i)) && !aabB(sb,str.charAt(i))) {
                sb.append(str.charAt(i));
            }
        }
        return sb.toString();


    }
    public boolean aaA(StringBuffer sb,char a) {
        int size = sb.length();
        if(size >= 2 && a == sb.charAt(size - 1) && sb.charAt(size - 1) == sb.charAt(size - 2)) {
            return true;
        }
        return false;
    }
    public boolean aabB(StringBuffer sb,char a) {
        int size = sb.length();
        if(size >= 3 && a == sb.charAt(size - 1) && sb.charAt(size - 2) == sb.charAt(size - 3)) {
            return true;
        }
        return false;
    }
}
```

此题的思路其实比较清晰。重点对于java中的StringBuffer的应用

- charAt 的应用可以找到String或者StringBuffer中的 char
- 利用append可以在StringBuffer后面添加新的元素。
- StringBuffer中的 toString( )可以得到新的String。

# 5. Leetcode 575

Given an integer array with 

even

 length, where different numbers in this array represent different 

kinds

 of candies. Each number means one candy of the corresponding kind. You need to distribute these candies 

equally

 in number to brother and sister. Return the maximum number of 

kinds

 of candies the sister could gain. 

**Example 1:**

```
Input: candies = [1,1,2,2,3,3]
Output: 3
Explanation:
There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too. 
The sister has three different kinds of candies. 
```

分糖果的题，给定的是一个偶数的数组，数组中的每一个元素数值代表的是某一个种类。要将这些糖果平均分给sis 和 bro，要求怎么能给sis最多种类的糖果。

- 因为是偶数的糖果个数，所以每个人的糖果个数是受限的 limit = size/2
- 建立一个sis的 hashmap 只要出现新的类型就给 sis 已经有的就不要了，并且时刻要判断 hashmap 的长度不要超过limit的数值。

```java
class Solution {
    public int distributeCandies(int[] candies) {
        int size = candies.length;
        if(size < 1) {
            return 0;
        }
        int limit = size / 2;
        HashMap<Integer,Integer> sis = new HashMap<>();
        for(int i = 0;i < size;i++) {
            if(sis.containsKey(candies[i])) {
                continue;
            }else {
                if(sis.size() < limit) {
                    sis.put(candies[i],1);
                }else {
                    break;
                }
            }
        }
        return sis.size();
    }
}
```

# 6. Leetcode 1005

Given an array `A` of integers, we **must** modify the array in the following way: we choose an `i` and replace `A[i]` with `-A[i]`, and we repeat this process `K` times in total.  (We may choose the same index `i` multiple times.)

Return the largest possible sum of the array after modifying it in this way.

 

**Example 1:**

```
Input: A = [4,2,3], K = 1
Output: 5
Explanation: Choose indices (1,) and A becomes [4,-2,3].
```

这道题的主要意思就是给你 K 个把给定 A 数组中元素变成它的相反数的机会并且每一个元素可以重复使用，最终使得整体的元素的和最大就行。所以我们的目标主要集中在：

- 尽量把负数变成正数。
- 如果没有负数有 0 的话就要把所有的机会用在0上。
- 没有零就要尽量把机会用在最小的数上，这样使得对整体的和影响的最小。

解决的思路是利用一个自动排序的队列**PriorityQueue**，最小的数在队列的顶上，将最小的数字 poll 变成相反数加入到原来的队列当中，重新排序，然后相同的操作直到机会K 用完。

- 如果是负数的话那么负数会变成正数加入到原来的数组中；
- 如果是 0 则会在0上不停的利用机会。
- 如果是最小的正数也会在上面利用完所有的机会。

```java
class Solution {
    public int largestSumAfterKNegations(int[] A, int K) {
        int size = A.length;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int a:A) {
            pq.add(a);
        }
        while(K-- > 0) {
            pq.add(-pq.poll());
        }
        int res = 0;
        for(int i = 0;i < size;i++) {
            res += pq.poll();
        }
        return res;
    }
}
```

# 7. Leetcode 144 (二叉树前序遍历)

针对二叉树的前序遍历，此时使用非递归的解法，那么必须利用的是栈（stack）：

- 首先将 root push 进 stack ；
- 将 root pop，同时将其中的 val 存入list中；
- 注意 stack 中的先入后出所以先将 rightNode 入栈，然后leftNode入栈。

前序遍历顺序：根/左/右

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
         Stack<TreeNode> st = new Stack<>();
        List<Integer> res = new ArrayList<>();
        //注意判空！
      	if(root == null) {
            return res;
        }
        st.push(root);
        while(!st.empty()) {
            TreeNode popedNode = st.pop();
            if(popedNode != null) {
                res.add(popedNode.val);
            }
            if(popedNode.right != null) {
                st.push(popedNode.right);
            }
            if(popedNode.left != null) {
                st.push(popedNode.left);
            }
        }
        return res;
    }
}
```

