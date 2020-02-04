[TOC]

# 1. Leetcode 1026（Tree/TopDown）

Given the `root` of a binary tree, find the maximum value `V` for which there exists **different** nodes `A` and `B` where `V = |A.val - B.val|` and `A` is an ancestor of `B`.

(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)

**Example 1:**

![img](http://i68.tinypic.com/2whqcep.jpg)

```
Input: [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: 
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
```

这个题的意思是说找到祖先节点和孩子节点的最大的差值：

- 最大的祖先节点数值 ➖ 最小的孩子节点的数值；
- 最大的孩子节点数值 ➖ 最小的祖先节点的数值；

所以整个的思路就在从上到下遍历树中的节点并且将当前得到的最大的节点的数值和最小的数值传递给下一个节点，在下一个节点计算：

- 最大的数值 - 当前的数值；
- 当前的数值 - 最小的数值；

由左右得到的最大数值和在上一层得到的最大差值求得一个最大的差值，返回；

```java
class Solution {
    public int maxAncestorDiff(TreeNode root) {
        return DFS(root,root.val,root.val);
    }
    public int DFS(TreeNode node,int mx,int mn) {
        if(node == null) {
            return 0;
        }
        int res = Math.max(mx - node.val,node.val - mn);
        mx = Math.max(node.val,mx);
        mn = Math.min(node.val,mn);
        res = Math.max(res,Math.max(DFS(node.left,mx,mn),DFS(node.right,mx,mn)));
        return res;
    }
}
```



# 2. Leetcode 508（Tree/Stack）

Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

**Examples 1**
Input:

```
  5
 /  \
2   -3
```

return [2, -3, 4], since all the values happen only once, return all of them in any order.



**Examples 2**
Input:

```
  5
 /  \
2   -5
```

return [2], since 2 happens twice, however -5 only occur once.

**Note:** You may assume the sum of values in any subtree is in the range of 32-bit signed integer.

子树的所有的节点（包括根节点）的和出现的次数作为子树出现的频率，要找到出现最多的频率是多少；

整个问题可以划分为两个阶段：

- 将所有的频率计算出来并存储在 HashMap 中；
  - 计算每一个节点和其根节点之和；
- 将 HashMap 中的"子树之和”和频率拿出来找到出现最多的一个或几个数值是多少；
  - 利用单调栈的特性，当当前的元素大于栈中的元素的时候，弹栈。
  - 当前的栈弹空说明该元素是最大的，入栈；
  - 当前的栈顶元素和当前的元素相同，说明出现的次数都是当前最大的；

```java
class Solution {
    public HashMap<Integer,Integer> map = new HashMap<>();
    public int[] findFrequentTreeSum(TreeNode root) {
        Stack<Integer> st = new Stack<>();
        DFS(root);
        for(int key:map.keySet()) {
            while(!st.isEmpty() && map.get(key) > map.get(st.peek())) {
                st.pop();
            }
            if(st.isEmpty() || map.get(key) == map.get(st.peek())) {
                st.push(key);
            }
        }
        int[] res = new int[st.size()];
        int i = 0;
        while(!st.isEmpty()) {
            res[i++] = st.pop();
        }
        return res;
    }
    public int DFS(TreeNode node) {
        if(node == null) {
            return 0;
        }
        int sum = node.val + DFS(node.left) + DFS(node.right);
        if(map.containsKey(sum)) {
            map.put(sum,map.get(sum) + 1);
        }else {
            map.put(sum,1);
        }
        return sum;
    }
}
```



# 3. Leetcode 572（Tree/两层递归）

Given two non-empty binary trees **s** and **t**, check whether tree **t** has exactly the same structure and node values with a subtree of **s**. A subtree of **s** is a tree consists of a node in **s** and all of this node's descendants. The tree **s** could also be considered as a subtree of itself.

**Example 1:**
Given tree s:

```
     3
    / \
   4   5
  / \
 1   2
```

Given tree t:

```
   4 
  / \
 1   2
```

Return 

true

, because t has the same structure and node values with a subtree of s.



**Example 2:**
Given tree s:

```
     3
    / \
   4   5
  / \
 1   2
    /
   0
```

Given tree t:

```
   4
  / \
 1   2
```

Return 

false

在一个树A里面找到是否存在另一个子树B；

- 递归在A中遍历每一个点，在每一个点进行判断是否是子树；
  - 每一个点进行判断如果A和B都是null，说明所有节点递归判断完成；
  - 如果一个为null，另一个不是说明存在不同的点，不是子树；
  - 数值不同不是子树；

```java
class Solution {
    public boolean isSubtree(TreeNode s, TreeNode t) {
        if(s == null) return false;
        if(same(s,t)) {
            return true;
        }else {
            return isSubtree(s.left,t) || isSubtree(s.right,t);
        }     
    }
    public boolean same(TreeNode s,TreeNode t) {
        if(s == null && t == null) return true;
        if(s == null || t == null) return false;
        if(s.val != t.val) {
            return false;
        }
        return same(s.left,t.left) && same(s.right,t.right);
    }
}
```



# 4. Leetcode 1028（Tree/Stack）

We run a preorder depth first search on the `root` of a binary tree.

At each node in this traversal, we output `D` dashes (where `D` is the *depth* of this node), then we output the value of this node.  *(If the depth of a node is D, the depth of its immediate child is D+1.  The depth of the root node is 0.)*

If a node has only one child, that child is guaranteed to be the left child.

Given the output `S` of this traversal, recover the tree and return its `root`.

 

**Example 1:**

**![img](https://assets.leetcode.com/uploads/2019/04/08/recover-a-tree-from-preorder-traversal.png)**

```
Input: "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]
```

**Example 2:**

**![img](https://assets.leetcode.com/uploads/2019/04/11/screen-shot-2019-04-10-at-114101-pm.png)**

```
Input: "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]
```

 

**Example 3:**

![img](https://assets.leetcode.com/uploads/2019/04/11/screen-shot-2019-04-10-at-114955-pm.png)

```
Input: "1-401--349---90--88"
Output: [1,401,null,349,88,90]
```

根据前序遍历的结果找到原来的树的样子，其中的"-"的个数代表的是和根节点（字符串的第一个字符）的距离；

这个题的思路的本质是一个Stack的类型题：

- 遍历整个字符串，判断"-"的个数决定当前的 level ，这个 level 是当前要加入树中的节点的层，所以为了将这个节点加入到父节点要利用栈提前将父节点存储起来；
  - 举个例子：如果1—2——3——4：1入栈，level为0，2入栈 level 为1，3入栈 level 为 2，但是此时的栈中有三个元素，弹栈得到父节点；
- 其余的操作都是从字符串中找到要利用的信息；

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
    public TreeNode recoverFromPreorder(String S) {
        int level = 0;
        int num = 0;
        Stack<TreeNode> st = new Stack<>();
        for(int i = 0;i < S.length();) {
            for(level = 0;S.charAt(i) == '-';i++) {
                level++;
            }
            for(num = 0;i < S.length() && S.charAt(i) != '-';i++) {
                num = num * 10 + (S.charAt(i) - '0');
            }
            while(st.size() > level) {
                st.pop();
            }
            TreeNode node = new TreeNode(num);
            if(!st.isEmpty()) {
                if(st.peek().left != null) {
                    st.peek().right = node;
                }else {
                    st.peek().left = node;
                }
            }
            st.push(node);
        }
        TreeNode root = new TreeNode(0);
        while(!st.isEmpty()) {
            root = st.pop();
        }
        return root;
    }
}
```

