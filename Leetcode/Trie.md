[TOC]

# Trie（前缀树）

## 1. Leetcode 208

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

这个题就是实现一个基本的前缀树的结构，可以通过这个题来了解简单的前缀树的功能；

从题目给的例子就可以看出，主要是一个方便存储和搜索的结构：

- 这棵树是一个多叉树，在本题中存储的字符串，所以一个节点有 26 个子节点分别代表着**a- z**；
- 将每一个字符串分别拆分成单个字符分别从根到叶子结点存储起来；
  - 因为会出现在寻找的过程中出现存储了“abcd”但是要寻找有没有"abc"这种情况，所以要加上一个判断该字符作为结尾是不是存在字符串的 boolean 值；

```java
class TreeNode {
    public TreeNode[] chi = new TreeNode[26];
    public boolean have = false;
}
class Trie {
    public TreeNode root = new TreeNode();
    /** Initialize your data structure here. */
    public Trie() {
    }
    
    /** Inserts a word into the trie. */
    public void insert(String word) {
        TreeNode node = root;
        for(char c:word.toCharArray()) {
            int pos = c - 'a';
            if(node.chi[pos] == null) {
                node.chi[pos] = new TreeNode();
            }
            node = node.chi[pos];
        }
        node.have = true;
    }   
    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        TreeNode node = root;
        int count = 0;
        int len = word.length();
        for(char c:word.toCharArray()) {
            int pos = c - 'a';
            if(node.chi[pos] == null) {
                return false;
            }
            count++;
            node = node.chi[pos];
        }
        if(count == len) {
            if(node.have == true) {
                return true;
            }else {
                return false;
            }
        }else {
            return false;
        }
    }
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        TreeNode node = root;
        int count = 0;
        int len = prefix.length();
        for(char c:prefix.toCharArray()) {
            int pos = c - 'a';
            if(node.chi[pos] == null) {
                return false;
            }
            count++;
            node = node.chi[pos];
        }
        if(count == len) {
            return true;
        }else {
            return false;
        }       
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

## 2. Leetcode 421

Given a **non-empty** array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ *i*, *j* < *n*.

Could you do this in O(*n*) runtime?

**Example:**

```
Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
```

找到两个数做异或操作的最大数值是什么，首先了解异或操作在每一位上都不同才能取得很好的结果：

- 首先将一个数字的二进制都存储在一棵树形结构中；
- 再次遍历一遍数组，每一次都尽量找和当前位不同的数字，如0 —> 1 / 1 —> 0；

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
        TreeNode root = new TreeNode(0);
        TreeNode node = root;
        for(int num:nums) {
            for(int i = 31;i >= 0;i--) {
                int val = num & (1 << i);
                if(val == 0) {
                    if(node.left == null) {
                        node.left = new TreeNode(0);
                    }
                    node = node.left;
                }else {
                    if(node.right == null) {
                        node.right = new TreeNode(1);
                    }
                    node = node.right;
                }
            }
            node = root;
        }
        int res = 0;int max = 0;
        node = root;
        for(int num:nums) {
            for(int i = 31;i >= 0;i--) {
                int val = num & (1 << i);
                if(val == 0) {
                    node = node.right == null?node.left:node.right; 
                }else {
                    node = node.left == null?node.right:node.left;
                }
                res += val ^ (node.val << i);
            }
            node = root;
            max = Math.max(res,max);
            res = 0;
        }
        return max;
    }
}
```

## 3. Leetcode 1032

Implement the `StreamChecker` class as follows:

- `StreamChecker(words)`: Constructor, init the data structure with the given words.
- `query(letter)`: returns true if and only if for some `k >= 1`, the last `k` characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.

**Example:**

```
StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
streamChecker.query('a');          // return false
streamChecker.query('b');          // return false
streamChecker.query('c');          // return false
streamChecker.query('d');          // return true, because 'cd' is in the wordlist
streamChecker.query('e');          // return false
streamChecker.query('f');          // return true, because 'f' is in the wordlist
streamChecker.query('g');          // return false
streamChecker.query('h');          // return false
streamChecker.query('i');          // return false
streamChecker.query('j');          // return false
streamChecker.query('k');          // return false
streamChecker.query('l');          // return true, because 'kl' is in the wordlist
```

主要是写一个StreamChecker，就是给定一个数组，你要判断到来的字符串中含有我们要的字符串；

- 首先将给定的字符串保存在一个 Trie 中，并且要倒着放入，比如"abc"—>"cba"；
- 将到来的一个一个的 letter 放在一个Stringbuilder 中（就是为了可以从最新得到的letter开始在Trie中寻找是不是有子串满足条件）；

```java
class StreamChecker {
    class TreeNode {
        public TreeNode[] chi = new TreeNode[26];
        public boolean have = false;
    }
    public StringBuilder sb = new StringBuilder();
    public TreeNode root = new TreeNode();

    public void getDicTree(String[] words) {
        for(String word:words) {
            int len = word.length();
            TreeNode node = root;
            for(int i = 1;i <= len;i++) {
                int pos = word.charAt(len - i) - 'a';
                if(node.chi[pos] == null) {
                    node.chi[pos] = new TreeNode();
                }
                node = node.chi[pos];
            }
            node.have = true;
        }
    }
    public StreamChecker(String[] words) {
        getDicTree(words);
        
    }  
    public boolean query(char letter) {
        sb.insert(0,letter);
        TreeNode node = root;
        for(char c:sb.toString().toCharArray()) {
            int pos = c - 'a';
            node = node.chi[pos];
            if(node == null) {
                return false;
            }
            if(node.have == true) {
                return true;
            }
        }
        return false;
    }
}
/**
 * Your StreamChecker object will be instantiated and called as such:
 * StreamChecker obj = new StreamChecker(words);
 * boolean param_1 = obj.query(letter);
 */
```

