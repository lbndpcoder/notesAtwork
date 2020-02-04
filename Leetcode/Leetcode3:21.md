[TOC]

#1. Leetcode 208（前缀树）

Implement a trie with `insert`, `search`, and `startsWith` methods.

**Example:**

```
Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
```

前缀树是一个多叉树，并且根结点对应子节点都不相同。主要是构造前缀树的数据结构：

```java
class TreeNode {
    public char val;
    public TreeNode[] children = new TreeNode[26];
    public boolean haveW = false; 
    public TreeNode(char c) {
        this.val = c;
    }
}
class Trie {
    public TreeNode root;
    /** Initialize your data structure here. */
    public Trie() {
        char c = ' ';
        this.root = new TreeNode(c);
    }   
    /** Inserts a word into the trie. */
    public void insert(String word) {
        TreeNode temp = this.root;
        for(char alpha:word.toCharArray()) {
            if(temp.children[alpha - 'a'] != null) {
                temp = temp.children[alpha - 'a'];
            }else {
                char n = alpha;
                TreeNode child = new TreeNode(n);
                temp.children[alpha - 'a'] = child;
                temp = child;
            }
        }
        temp.haveW = true;
    }
    /** Returns if the word is in the trie. */
    public boolean search(String word) {
       TreeNode temp = this.root;
       int count = 0;
       for(char alpha:word.toCharArray()) {
           if(temp.children[alpha - 'a'] != null) {
               temp = temp.children[alpha - 'a'];
               count += 1;
           }
       }
       if(count < word.length()) {
           return false;
       }else {
           if(temp.haveW == true) {
               return true;
           }else {
               return false;
           }
       }
    }
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        TreeNode temp = this.root;
        int count = 0;
        for(char alpha:prefix.toCharArray()) {
            if(temp.children[alpha - 'a'] != null) {
                temp = temp.children[alpha - 'a'];
                count += 1;
            }
        }
        if(count == prefix.length()) {
            return true;
        }
        return false;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */
```

# 2. Leetcode 421（前缀树）

Given a **non-empty** array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 2^31.

Find the maximum result of ai XOR aj, where 0 ≤ *i*, *j* < *n*.

Could you do this in O(*n*) runtime?

**Example:**

```
Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
```

通过构造深度为32的前缀树来找到每一个数值的最大异或值；

- 首先构造前缀树，利用的是每一个数的二进制，最高位在树的顶端，如果为0那么成为右孩子，如果为1那么成为左孩子；
- 通过构造出来的前缀树遍历每一个数字找到最佳的异或值，假如一位是 0，那么最佳的异或数值此位就是1，一直遍历到叶子结点并在遍历的时候计算出异或数值；

```java
class TreeNode {
    public TreeNode left;
    public TreeNode right;
    public int val;
    public TreeNode(int val) {
        this.val = val;
    }
}
class Solution {
    public int findMaximumXOR(int[] nums) {
        int size = nums.length;
        TreeNode root = new TreeNode(0);
        TreeNode cur = root;
        for(int i = 0;i < size;i++) {
            int temp = nums[i];
            for(int j = 31;j >= 0;j--) {
                int val = temp & (1 << j);
                if(val == 0) {
                    if(cur.right == null) {
                        cur.right = new TreeNode(0);
                    }
                    cur = cur.right; 
                }else {
                    if(cur.left == null) {
                        cur.left = new TreeNode(1);
                    }
                    cur = cur.left;
                }
            }
            cur = root;
        }
        int max = 0;
        int res = 0;
        cur = root;
        for(int i = 0;i < size;i++) {
            res = 0;
            int temp = nums[i];
            for(int j = 31;j >= 0;j--) {
                int val = temp & (1 << j);
                if(cur.left != null && cur.right != null) {
                   if(val == 0) {
                       cur = cur.left;
                   }else {
                       cur = cur.right;
                   }
                }else {
                    cur = cur.left != null ? cur.left:cur.right; 
                }
                res += val ^ (cur.val << j);
            }
            cur = root;
            max = Math.max(res,max);
        }
        return max;
    }
}
```

# 3. 2018 蚂蚁内推笔试算法

给一个圆，分成M份，有N个颜色，相邻的扇形颜色不能相同，一共多少种；

- 用递归，第一块有N个颜色选用，第二个（N-1）第三个（N-1）直到最后一个（N-1）；
- 但是此时最后和开始的一样颜色了所以需要减去他俩一样的这种情况的种类就相当于是M-1份用N个颜色填充的种类；

```java
public class main {
    public static void main(String[] args) {
    //主要查看在笔试的时候输入怎么写；  
      Scanner scan = new Scanner(System.in);
      int m = scan.nextInt();
      int n = scan.nextInt();
      CircleColor cc = new CircleColor();
      int res = cc.kinds(4,3);
      System.out.println(res);
    }
}
public class CircleColor {
    public int kinds(int m,int n) {
        if(m == 1) {
            return n;
        }
        if(m == 2) {
            return n*(n - 1);
        }
        if(m == 3) {
            return n * (n - 1) * (n - 2);
        }
        int number = 0;
        if(m > 3) {
             number = n * (int)Math.pow(n - 1,m - 1) - kinds(m - 1,n);
        }
        return number;
    }
}
```

