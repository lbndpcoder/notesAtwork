[TOC]

# 1. Leetcode 589（n叉树前序遍历）

Given an n-ary tree, return the *preorder* traversal of its nodes' values.

n叉树的前序遍历，不用递归的话利用stack：

- 首先将 root 入栈，然后弹出栈顶的元素；
- 将栈顶的元素从子节点的最后一个开始加入栈，栈是先进后出的，所以把先遍历的点后进入；

```java
class Solution {
    public List<Integer> preorder(Node root) {
        Stack<Node> st = new Stack<>();
        st.push(root);
        List<Integer> res = new ArrayList<>();
        if(root == null) {
            return res;
        }
        while(!st.empty()) {
            Node cur = st.pop();
            res.add(cur.val);
            int size = cur.children.size();
            for(int i = size - 1;i >= 0;i--) {
                st.push(cur.children.get(i));
            }
        }
        return res;
    }
}
```

# 2. Leetcode 395（*）

Find the length of the longest substring **T** of a given string (consists of lowercase letters only) such that every character in **T** appears no less than *k*times.

**Example 1:**

```
Input:
s = "aaabb", k = 3
Output:
3
The longest substring is "aaa", as 'a' is repeated 3 times.
```

给定一个字符串找到子串，子串中的元素所有的元素都需要重复 >=k 次：

- 将字符串中的每一个元素出现的次数记录下来，设置一个长度为26的数组；
- 如果一个字符出现的次数满足要求，那么要找的子串一定在一个以某一个满足要求的字符的第一次出现的位置开始，以某一个满足要求的字符的最后一次出现的位置为止；
- 找到一个大概的范围之后，找到其中不满足条件的异常点（出现次数不满条件的字符）；
  - 从不满足条件的左侧开始寻找；substring（low，i）；
  - 从不满足条件的右侧开始寻找；substring（i+1，high+1）
- 如果没有不满足条件的点就返回子串的长度；

```java
class Solution {
    public int longestSubstring(String s, int k) {
        if(k < 1 || s.length() < 1) {
            return 0;
        }
        int[] record = new int[26];
        for(char c:s.toCharArray()) {
            record[c - 'a'] += 1;
        }        
        int length = s.length();
        int low = Integer.MAX_VALUE;
        int high = Integer.MIN_VALUE;
        boolean f = false;
        for(int i = 0;i < length;i++) {
            if(record[s.charAt(i) - 'a'] >= k) {
                f = true;
                if(low > i) {
                    low = i;
                }
                if(high < i) {
                    high = i;
                }
            }
        }
        if(f) {
            for(int i = low;i <= high;i++) {
                if(record[s.charAt(i) - 'a'] < k) {
                    return Math.max(longestSubstring(s.substring(low,i),k),
                                    longestSubstring(s.substring(i + 1,high +1),k));
                }
            }
        }
        return f?high - low + 1:0;
    }
}
```

# 3. Leetcode 124（hard*）

Given a **non-empty** binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain **at least one node** and does not need to go through the root.

找到树中的路径最大值，找到一条不能回头的路径上的数值最大：

- 可以是一个子树作为最大值；
- 可以是从左侧到根不去右侧向上走；
- 可以是从右侧到根不去左侧向上走；

解决的思路就是：

- 设置一个全局的变量用来监测当前的子树左+右+根的数值是否最大；
- 如果无论从左或者右来的数值都小于0的话说明这侧来的数值可以不用就是变为0；

整体来说就是4个数值：

- left + right + root（不能带到上一层用来更新全局）
- left + root
- right + root
- root

第一个版本比较简单容易看：

```java
class Solution {
    public int max = Integer.MIN_VALUE;
    public int maxPathSum(TreeNode root) {
        if(root == null) {
            return 0;
        }
        int a = helper(root);
        return this.max;
    }
    public int helper(TreeNode root) {
        if(root == null) {
            return 0;
        }
        int left = helper(root.left);
        int right = helper(root.right);
        int rootVal = root.val;
        
        int lr = left + rootVal;
        int lrr = left + right + rootVal;
        int rr = right + rootVal;
        
        this.max = maxFour(this.max,lr,lrr,rr,rootVal);
        
        return maxThree(lr,rr,rootVal);
    }
    public int maxFour(int a,int b,int c,int d,int e) {
        int[] record = {a,b,c,d,e};
        Arrays.sort(record);
        return record[4];
    }
    public int maxThree(int a,int b,int c) {
        int[] record = {a,b,c};
        Arrays.sort(record);
        return record[2];
    }
}
```

第二个版本思路一样进行优化：

```java
class Solution {
    public int max = Integer.MIN_VALUE;
    public int maxPathSum(TreeNode root) {
        if(root == null) {
            return 0;
        }
        helper(root);
        return this.max;
    }
    public int helper(TreeNode root) {
        if(root == null) {
            return 0;
        }
        int left = helper(root.left);
        int right = helper(root.right);
        int rv = root.val;
        this.max = Math.max(max,rv + left + right);
        int cur = rv + Math.max(left,right);
        return cur > 0 ? cur:0;
    }
}
```



