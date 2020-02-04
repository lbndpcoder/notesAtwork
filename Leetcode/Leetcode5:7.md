[TOC]

# BST

## 1. Leetcode 938

Given the `root` node of a binary search tree, return the sum of values of all nodes with value between `L` and `R`(inclusive).

The binary search tree is guaranteed to have unique values.

**Example 1:**

```
Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
```

在给定的一个 BST 中找到L与R范围内的数的和；

- 充分利用 BST 的信息；
  - 就是如果当前的节点的数值小于L，那么要找的数值一定就是在当前的节点的右侧节点；
  - 大于R，一定在当前的节点的左侧；
- 遍历一遍树； 

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
    public int res = 0;
    public int rangeSumBST(TreeNode root, int L, int R) {
        helper(root,L,R);
        return res;
    }
    public void helper(TreeNode node,int L,int R) {
        if(node == null) return;
        if(node.val < L) {
            helper(node.right,L,R);
        }else if(node.val > R) {
            helper(node.left,L,R);
        }else {
            res += node.val;
            helper(node.right,L,R);
            helper(node.left,L,R);
        }
    }
}
```

## 2. Leetcode 1038（R）

# String

## Leetcode 6

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: `"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a number of rows:

```
string convert(string s, int numRows);
```

**Example 1:**

```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```

主要的思路就是将给定的字符串按照给定的方式排入字符数组当中，然后再按照行遍历；

- 注意的是当 size 为 0 的时候要返回空；
- 当字符串的长度小于 n 的时候直接返回原来的字符串；
- 当只有一行的时候同理；

```java
class Solution {
    public String convert(String s, int n) {
        int size = s.length();
        if(size == 0) return new String("");
        if(size <= n || n == 1) return s;
        int col = size / 2;
        int addedCol = size % (2 * n - 2) > n?size % (2 * n - 2) - n + 1:1;
        col += addedCol;
        char[][] ch = new char[n][col];
        int count = 0;
        int i = 0;int j = 0;
        for(char c:s.toCharArray()) {
            ch[i][j] = c;
            if(i == 0 || i== n - 1) {
                count += 1;
                count %= 2;
            }
            if(count == 0) {
                i--;
                j++;
            }else {
                i++;
            }
        }
        count = 0;
        char[] res = new char[size];
        for(i = 0;i < n;i++) {
            for(j = 0;j <col;j++) {
                if(ch[i][j] != '\u0000') {
                    res[count++] = ch[i][j];
                }
            }
        }
        return String.valueOf(res);
    }
}
```

