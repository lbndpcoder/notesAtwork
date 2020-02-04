[TOC]

#1. Leetcode 108（BST）

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of *every*node never differ by more than 1.

**Example:**

```
Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
```

本题是一个有序数组怎么构造一个BST（二叉排序树）二叉排序树就是：

二叉排序树(简称BST)的定义为:二叉排序或者是空树,或者是满足如下性质的二叉树:

- 若他的左子树非空,则左子树上所有记录的值均小于根记录的值；
- 若他的右子树非空,则右子树上所有记录的值均大于根记录的值；
- 左,右子树本身又各是一棵二叉排序树；

以为你给定的是一个有序的数组所以在解决本题的时候就会简单很多：

- 找到整个数组的中间位置 mid 的数值作为整棵树的 root 的 val ；
- 不断的递归得到左面的 mid，作为左子树的 root ；
- 递归右侧的 mid 作为右子树的 root； 

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
    public TreeNode sortedArrayToBST(int[] nums) {
        if(nums.length == 0) {
            return null;
        }
        return buildTree(nums,0,nums.length - 1);
    }
    public TreeNode buildTree(int[] nums,int start,int end) {
        if(start > end) {
            return null;
        }
        int mid = start + (end - start) / 2;
        TreeNode tempRoot = new TreeNode(nums[mid]);
        tempRoot.left = buildTree(nums,start,mid - 1);
        tempRoot.right = buildTree(nums,mid + 1,end);
        return tempRoot;
    }
}
```

# 2. Leetcode 450（BST）

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

1. Search for a node to remove.
2. If the node is found, delete the node.

删除 BST 中的一个节点，主要分两个步骤：

- 找到这个节点：
  - 如果 key 小于当前节点 val 那么要寻找的节点在当前节点的 left ；
  - 如果 key 大于当前节点的 val 那么就在 right ；

- 删除这个节点：
  - 如果当前节点的左或者右有一个为 null 只需要直接返回非空的那一侧；
  - 如果两侧都不空，那么找到右侧节点的最小 val 的节点，作为当前节点的替换节点；
  - 替换之后需要对删除的节点（找到的新的节点替换之前删除的那个节点的节点）进行删除；

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
    public TreeNode deleteNode(TreeNode root, int key) {
        if(root == null) {
            return null;
        }
        if(key < root.val) {
            root.left = deleteNode(root.left,key);
        }else if(key > root.val) {
            root.right = deleteNode(root.right,key);
        }else {
            if(root.left == null) {
                return root.right;
            }else if(root.right == null) {
                return root.left;
            }
            TreeNode minNode = findMin(root.right);
            root.val = minNode.val;
            root.right = deleteNode(root.right,minNode.val);
        }
        return root;     
    }
    public TreeNode findMin(TreeNode root) {
        while(root.left != null) {
            root = root.left;
        }
        return root;
    }
}
```

