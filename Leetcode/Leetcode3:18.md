[TOC]

# 1. Leetcode 94（二叉树中序遍历）

二叉树的中序遍历主要思路如下：

- 如果左节点不为空，将左节点加入 stack ；
- 如果左节点为空，将当前元素 pop 将数值加入到 res ；
- 如果右节点不为空，将 rightNode push stack 中；
- 如果右节点为空直接pop stack 顶端元素；

总结就是入栈的时候向左走，判断left是否为空；

出stack的时候向右走，判断right是不是为空；

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
    public List<Integer> inorderTraversal(TreeNode root) {
        Stack<TreeNode> st  = new Stack<>();
        List<Integer> res = new ArrayList<>();
        while(!st.empty() || root != null) {
            if(root != null) {
                st.push(root);
                root = root.left;
            }else {
                root = st.pop();
                res.add(root.val);
                root = root.right;
            }
        }
        return res; 
    }
}
```

# 2. Leetcode 3

Given a string, find the length of the **longest substring** without repeating characters.

**Example 1:**

```
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
```

找到给定字符串中的最大子串并且要求其中没有重复的元素。

- 声明一个足够大的数组 [233] 用来存储元素是否出现过；

- 找到两个指针 i ，j；
- 第一个指针 i 向前移动，判断当存在已经存在过的元素，说明在 j 和 i 之间的字符串存在这个元素，所以将 j 向前移动并把在i，j之外的元素释放掉（从出现过变成没有出现过），直到当前i所处的位置的元素第一次出现，比较是否为最长的元素。

```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int[] have = new int[128];
        int max = 0;
        int size = s.length();
        if(size <= 1) {
            return size;
        }
        int j = 0;
        for(int i = 0;i < size;i++) {
            while(have[s.charAt(i)] != 0 && j < i) {
                have[s.charAt(j)] = 0;
                j++;
            } 
            have[s.charAt(i)] = 1;
            max = Math.max(max,i - j + 1);
        }
        return max;
    }
}
```

注意问题是测试用例中具有很多的？！空格这种，所以声明的判断是否存在的数组要足够大为128是常用的ASCII码的范围。