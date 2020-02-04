[TOC]

# 1 . Leetcode 76

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

**Example:**

```
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
```

找到包含目标 T 中的字符的最小的子串；只要有就行不需要顺序；主要的思想是利用两个指针和一个 HashMap；

- HashMap 中存储的是目标 T 中的所有的字符以及数量；<Character,Integer>;
- left，right 两个指针；

整个流程：

- 首先是right指针不断的向右移动；
  - 如果遇到T中包含的字符，那么将map中的字符个数减 1 ；
  - 每一次的遇到map中的字符，并且map中对应的字符个数没有"用尽”，那么count++；
  - map中所有字符都已遍历到了说明此时的 right 和left之间的字符串就是满足条件但不是最短的子串；
- left指针向右移动，如果找到的字符串的字符放回原来的 map 中；
  - 如果放回之后不满足条件那么 right 继续移动；
  - 如果满足条件说明这个时候是最短的更新 minLeft 和 minLength；
- 如果最后得到的minLength比整个字符串的长度还长（初始值的设定）说明没有满足条件，返回""；

```java
class Solution {
    public String minWindow(String s, String t) {
        HashMap<Character,Integer> map = new HashMap<>();
        for(char c:t.toCharArray()) {
            if(map.containsKey(c)) {
                map.put(c,map.get(c) + 1);
            }else {
                map.put(c,1);
            }
        }
        int left = 0;int right = 0;int minl = 0;
        int minLength = s.length() + 1;
        int count = 0;
        while(right < s.length()) {
            char rightValue = s.charAt(right);
            if(map.containsKey(rightValue)) {
                map.put(rightValue,map.get(rightValue) - 1);
                if(map.get(rightValue) >= 0) {
                    count++;
                }
                 while(count == t.length()) {
                if(right - left + 1< minLength) {
                    minl = left;
                    minLength = right - left + 1;
                }
                char leftValue = s.charAt(left);
                if(map.containsKey(leftValue)) {
                    map.put(leftValue,map.get(leftValue) + 1);
                    if(map.get(leftValue) > 0) {
                        count--;
                    }
                }
                left++;
            }
            }
            right++;
        }
        if(minLength > s.length()) {
            return "";
        }
        return s.substring(minl,minl+minLength); 
    }
}
```

# 2. Leetcode 1022

Given a binary tree, each node has value `0` or `1`.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is `0 -> 1 -> 1 -> 0 -> 1`, then this could represent `01101` in binary, which is `13`.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers.

**Example 1:**

![img](https://assets.leetcode.com/uploads/2019/04/04/sum-of-root-to-leaf-binary-numbers.png)

```
Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
```

不算一道很难的题，主要就是根据每一条从root到leaf的路径上组成的二进制数转换成十进制之后进行求和；

- 从根节点逐渐利用二进制转十进制的方法；val = val * 2 + node.val ；
- 如果左右的节点都是 null ，那么说明是叶子结点，计算结束；
- 如果节点是 null 返回 0；
- 分别从左子树，右子树计算；

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
    public int sumRootToLeaf(TreeNode root) {
        return helper(root,0);
    }
    public int helper(TreeNode node,int val) {
        if(node == null) {
            return 0;
        }
        val = val * 2 + node.val;
        if(node.left==null && node.right==null) {
            return val; 
        }
        int left = helper(node.left,val);
        int right = helper(node.right,val);
        return (left+right);
    }
}
```

