[TOC]

# 1.Leetcode 503（stack：下一个最大的数）



Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

**Example 1:**

```
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
```

题目的描述是找到**下一个最大的数值**并且是一个循环的数组（首尾相接），解决方法是利用栈：

- 用一个栈从数组的尾部的 index 开始存储一直存储到头部[n-1,n-2,n-3,….,0]
- 所以栈的peek就是数组第一个数值；
- 从尾部开始比较，不断的比较数组的第一个数值和当前数值的大小，如果小的话就弹出栈，直到找到一个大于此时比较的数值；
- 将当前的index加入到栈中：
  - 如果下一个数值小于当前的数值那么下一个最大值就是当前数值；
  - 如果下一个大于当前数值，那么也没有必要比较比当前数值小的数；

```java
class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int size = nums.length;
        Stack<Integer> st = new Stack<>();
        for(int i = size - 1;i >= 0;i--) {
            st.push(i);
        }
        int[] res = new int[size];
        for(int i = size - 1;i >= 0;i--) {
            res[i] = -1;
            while(!st.isEmpty() && nums[st.peek()] <= nums[i]) {
                st.pop();
            }
            if(!st.isEmpty()) {
                res[i] = nums[st.peek()]; 
            }
            st.push(i);
        }
        return res;
    }
}
```

# 2 . Leetcode 739（stack：下一个最大的数）

Given a list of daily temperatures `T`, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put `0`instead.

For example, given the list of temperatures `T = [73, 74, 75, 71, 69, 72, 76, 73]`, your output should be `[1, 1, 4, 2, 1, 1, 0, 0]`.

**Note:** The length of `temperatures` will be in the range `[1, 30000]`. Each temperature will be an integer in the range `[30, 100]`.

都是找到下一个最大的数，整体的思路都是利用的stack来减少整体的时间复杂度：

- 利用栈存储数组的 index；
- 如果新来的数字（遍历一遍数组）大于当前栈顶的数字，那么说明栈顶的数字的下一个最大值就是这个新来的数字，新来的数字的index = i；
- 然后从栈顶向下寻找是否这个新来的还是其他的下一个最大数字，如果是那么就不断的弹栈；
- 如果循环停止，说明有一个元素的数值很大当前的数值还不够，把当前的数值放入栈中；

```java
class Solution {
    public int[] dailyTemperatures(int[] T) {
        int size = T.length;
        int[] res = new int[size];
        Stack<Integer> st = new Stack<>();
        for(int i = 0;i < size;i++) {
            while(!st.isEmpty() && T[i] > T[st.peek()]) {
                int index = st.pop();
                res[index] = i - index;
            }
            st.push(i);
        }
        return res;
    }
}
```

# 3. Leetcode 496（stack：下一个最大的数）

You are given two arrays **(without duplicates)** `nums1`and `nums2` where `nums1`’s elements are subset of `nums2`. Find all the next greater numbers for `nums1`'s elements in the corresponding places of `nums2`. 

The Next Greater Number of a number **x** in `nums1` is the first greater number to its right in `nums2`. If it does not exist, output -1 for this number.

**Example 1:**

```
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
```

这个还是找下一个最大数的一个题，利用 stack，目标是找到在 nums2 中的 nums1 中的元素的下一个最大数值，其实利用map和stack的组合可以解决：

- 利用 stack 找到 nums2 中每一个元素的下一个最大的数值，如果不存在就变成-1；
  - 每出现一个新的元素就和栈顶的元素进行比较；
  - 如果大于栈顶的元素说明新出现的元素是栈顶的下一个最大值，并pop（）；
  - 比较下一个栈顶元素是否成立；
  - 也就是说每出现的一个新元素放在栈顶都是最小的元素，下面的元素都是这个元素没办法handle的；
- 因为 nums1 中的数值都存在于 nums2 中所以可以知道nums1中的元素在nums2中的下一个最大值是什么；

```java
class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        HashMap<Integer,Integer> map = new HashMap<>();
        for(int a:nums1) {
            map.put(a,-1);
        }
        Stack<Integer> st = new Stack<>();
        for(int i = 0;i < nums2.length;i++) {
            while(!st.isEmpty() && nums2[i] > st.peek()) {
                int temp = st.pop();
                if(map.containsKey(temp)) {
                    map.put(temp,nums2[i]);
                }
            }
            st.push(nums2[i]);
        }
        int[] res = new int[nums1.length]; 
        int index = 0;
        for(int a:nums1) {
            res[index++] = map.get(a);
        }        
        return res;
    }
}
```

# 4. Leetcode 1019（stack：下一个最大的数）

We are given a linked list with `head` as the first node.  Let's number the nodes in the list: `node_1, node_2, node_3, ...`etc.

Each node may have a *next larger* **value**: for `node_i`, `next_larger(node_i)` is the `node_j.val` such that `j > i`, `node_j.val > node_i.val`, and `j` is the smallest possible choice.  If such a `j` does not exist, the next larger value is `0`.

Return an array of integers `answer`, where `answer[i] = next_larger(node_{i+1})`.

Note that in the example **inputs** (not outputs) below, arrays such as `[2,1,5]` represent the serialization of a linked list with a head node value of 2, second node value of 1, and third node value of 5

**Example 1:**

```
Input: [2,1,5]
Output: [5,5,0]
```

就是一样的意思只是给的是链表，把链表变成ArrayList进行相同的操作；

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public int[] nextLargerNodes(ListNode head) {
        Stack<Integer> st = new Stack<>();
        int length = 0;
        ListNode cur = head;
        List<Integer> l = new ArrayList<>();
        for(ListNode node = head;node != null;node = node.next) {
            l.add(node.val);
        }
        int[] res = new int[l.size()];
        for(int i = 0;i < l.size();i++) {
            res[i] = 0;
            while(!st.isEmpty() && l.get(st.peek()) < l.get(i)) {
                res[st.pop()] = l.get(i);
            }
            st.push(i);
        }
        return res;
    }
}
```

