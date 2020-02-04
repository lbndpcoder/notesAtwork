[TOC]

# 1. Leetcode 98 （BST：判断）

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

- The left subtree of a node contains only nodes with keys **less than** the node's key.
- The right subtree of a node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.

就是判断是不是二叉排序树：

- 左子树的所有数值都要比根节点的数值要小；
- 右子树的所有数值都要比根节点的数值要大；

整体的思路就是向左走标记当前的数值为最大值，后续的节点都要小于这个数值。向右走的话标记为最小值，后续的节点都要比这个数值要大；

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
    public boolean isValidBST(TreeNode root) {
        return helper(root,Long.MAX_VALUE,Long.MIN_VALUE);     
    }
    public boolean helper(TreeNode root,long max,long min) {
        if(root == null){
            return true;
        }
        if(root.val >= max || root.val <= min) {
            return false;
        }
        return helper(root.left,root.val,min) && helper(root.right,max,root.val);
    }
}
```

#2. Leetcode 173（BST：迭代器）

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling `next()` will return the next smallest number in the BST.

**Example:**

**![img](https://assets.leetcode.com/uploads/2018/12/25/bst-tree.png)**

```
BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
```

写一个 BST 的迭代器，基本规则和例子相同，主要的思路：

- 利用栈进行存储每一个节点；
- 将节点从根到它的左孩子全部入栈；
- 弹出的时候的 val 就是 next 的返回值；
- 弹出之后如果被弹出的节点的右孩子不为空那么将右孩子和它的左孩子继续入栈；
- 判断栈是不是为空用来判断有没有下一个数值；

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
class BSTIterator {
    public Stack<TreeNode> st = new Stack();
    public BSTIterator(TreeNode root) {
        if(root != null) {
            this.st.push(root);
        }
        while(root!=null && root.left != null) {
            st.push(root.left);
            root = root.left;
        }    
    }   
    /** @return the next smallest number */
    public int next() {
        TreeNode temp = st.pop();
        if(temp.right != null) {
            TreeNode tempR = temp.right;
            while(tempR != null) {
                this.st.push(tempR);
                tempR = tempR.left;
            }
        }
        return temp.val;
    }   
    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        if(!st.empty()) {
            return true;
        }else {
            return false;
        }       
    }
}
/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */
```

#3. Leetcode 700（BST：搜索）

Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

**很简单**就是利用BST的特性找到给定值的节点就可以；

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
    public TreeNode searchBST(TreeNode root, int val) {
        if(root == null) {
            return null;
        }
        TreeNode curNode = root;
        while(curNode != null) {
            if(curNode.val == val) {
                break;
            }
            if(val > curNode.val) {
                curNode = curNode.right;
            }else if(val < curNode.val) {
                curNode = curNode.left;
            }
        }
        return curNode;
    }
}
```

# 4. Leetcode 701（BST：插入）

Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

对 BST 进行插入一个新的数值，这个数值直接是叶子结点。所以找到这个位置是比较重要的，并且需要知道是左孩子还是右孩子；

```java
class Solution {
    public TreeNode insertIntoBST(TreeNode root, int val) {
        TreeNode cur = root;
        TreeNode last = cur;
        int rl= 0;
        while(cur!= null) {
            last = cur;
            if(val > cur.val) {
                rl = 0;
                cur = cur.right;
            }else if(val < cur.val) {
                rl = 1;
                cur = cur.left;
            }else {
                return cur;
            }
        }
        cur = new TreeNode(val);
        if(rl == 0) {
            last.right = cur;
        }else {
            last.left = cur;
        }
        return root;
    }
}
```

