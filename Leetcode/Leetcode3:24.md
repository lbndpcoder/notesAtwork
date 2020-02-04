[TOC]

# 1. Leetcode 703

Design a class to find the **k**th largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your `KthLargest` class will have a constructor which accepts an integer `k` and an integer array `nums`, which contains initial elements from the stream. For each call to the method `KthLargest.add`, return the element representing the kth largest element in the stream.

**玩文字游戏**。。。找的是第K大的元素，意思是最大的元素假如是7，8，9所以第三大的元素就是7；

- 使用一个 PriorityQueue 容器，每次保留K个元素；
- 输出队列的peek；

```java
class KthLargest {
    public PriorityQueue<Integer> pq;

    int kth;
    public KthLargest(int k, int[] nums) {
        this.pq = new PriorityQueue<>();
        this.kth = k;
        for(int num:nums) {
            this.pq.offer(num);
        }
    }
    
    public int add(int val) {
        this.pq.offer(val);
        int temp = this.kth;
        while(pq.size() > temp) {
            pq.poll();
        }
        return pq.peek();
    }
}
/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */
```

# 2. Leetcode 236（二叉树最近公共祖先）

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow **a node to be a descendant of itself**).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]



![binarytree](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

找到两个节点的最近的公共祖先节点；

- 递归出口是找到的节点为 null 或者 val 是两个数值中的一个然后返回当前的节点；
- 递归向左找或者向右找；
- 并且在当前节点进行总结：
  - 如果左右都不是空说明当前节点就是公共的祖先节点；
  - 如果任意一侧不是空，就说明找到了一个数值直接返回这个节点就可以了；

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
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root == null) {
            return null;
        }
        if(root.val == p.val || root.val == q.val) {
            return root;
        }
        TreeNode left =  lowestCommonAncestor(root.left,p,q);
        TreeNode right =  lowestCommonAncestor(root.right,p,q);
        if(left != null && right != null) {
            return root;
        }else if(left != null) {
            return left;
        }else if(right != null){
            return right;
        }else {
            return null;
        }
    }
}
```

# 3. Leetcode 235（BST最近公共祖先）

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow **a node to be a descendant of itself**).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]

和上面的不同这里的树是BST，二叉搜索树，思路大概是：

- 如果当前的节点的数值是两个数之间的数那么就说明这个点就是所找的数值；
- 只要存在一个数值等于当前的节点的数值当前节点就是所找的数值；
- 如果这个数值小于两个数值那么所找的中间点在右子树；
- 大于两个数所找的点在左子树；

```java
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        while(root != null) {
            if(Math.min(p.val,q.val) < root.val && Math.max(p.val,q.val) > root.val) {
                return root;
            }
            if(root.val == p.val || root.val == q.val) {
                return root;
            }
            if(root.val < Math.min(p.val,q.val)) {
                root = root.right;
            }else if(root.val > Math.max(p.val,q.val)) {
                root = root.left;
            }
        }
        return root;  
    }
}
```

