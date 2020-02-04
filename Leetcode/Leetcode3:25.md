[TOC]

# 1. Leetcode 220（BST：TreeSet）

Given an array of integers, find out whether there are two distinct indices *i*and *j* in the array such that the **absolute**difference between **nums[i]** and **nums[j]**is at most *t* and the **absolute** difference between *i* and *j* is at most *k*.

给一个数组要求找到其中距离 <= k 的两个位置上的数字的差最多为 t：

- 可以设置一个大小为 k 的窗口；
- 在每一个窗口中利用 TreeSet 的数据结构存储找到是否存在在 nums[i] + t 和 nums[i] - t 之内的数值；
- 超过窗口的数值去掉；

注意使用Long，测试中有long；

```java
class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, long t) {
        TreeSet<Long> window = new TreeSet<Long>();
        int size = nums.length;
        for(int i = 0;i < size;i++) {
            if ( window.floor(nums[i] + t) !=null && window.floor(nums[i]+t) >= nums[i]-t ) {
                return true;
            }
            window.add(new Long(nums[i]));
            if(i >= k) {
                window.remove(new Long(nums[i - k]));
            }
        }
        return false;
    }
}
```

TreeSet 中的 floor 表示找到的是小于或等于给定元素的最大数值；

# 2. Leetcode 110（是否为平衡二叉树）

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

> a binary tree in which the depth of the two subtrees of *every* node never differ by more than 1.

判断一个二叉树是否为平衡二叉树，就是判断一个二叉树左右的节点的高度是否相差小于1；

- 叶子结点的高度为1；
- 判断每一个节点的左右节点的高度，如果在范围内：就是相差的高度的绝对值小于1；
- 如果小于1那么看左边的高还是右侧的高或者相同，当前的高度为较高的数值+1；

```java
class Solution {
    public boolean b = true;
    public boolean isBalanced(TreeNode root) {
        int res = helper(root);
        return this.b;   
    }
    public int helper(TreeNode root) {
        if(b) {
            if(root == null) {
                return 0;
            }
            if(root.left == null && root.right == null) {
                return 1;
            }
            int left = helper(root.left);
            int right = helper(root.right);
            if(Math.abs(left - right) <= 1) {
                if(left > right) {
                    return left + 1;
                }else {
                    return right + 1;
                }
            }else {
                this.b = false;
                return 0;
            }
        }else {
            return 0;
        }
    }    
}
```

# 3.Leetcode 104（二叉树的深度）

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Note:** A leaf is a node with no children.

很简单的题，，和上一个思路一样；修改一下，返回不用判断返回的是较大的深度+1；

```java
class Solution {
    public int maxDepth(TreeNode root) {
        if(root == null) {
            return 0;
        }
        if(root.left == null && root.right == null) {
            return 1;
        }
        int left = maxDepth(root.left);
        int right = maxDepth(root.right);
        return Math.max(right,left) + 1;
    }
}
```

