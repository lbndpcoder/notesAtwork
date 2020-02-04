[TOC]

# HashSet/HashMap 实现

## 1. Leetcode 705 (HashSet实现)

这个题其实不用很麻烦的方法也可以构建一个HashSet，但是在这里正好复习 BST 的用法利用一个BST来构建HashSet：

- 整体的结构是一个由**BST**组成的数组：
  - 用树的结构可以避免重复的数值SET；
  - 可以快速的查找数值；
- 并且设计了一个 rehash，当添加的数值的数量超过一定数组长度的比率的时候就rehash；

```java
class MyHashSet {
    public int eleNum;
    public BSTNode[] shelf;
    final static int initialNum = 1;
    final static double rehashRate = 0.7;
    /** Initialize your data structure here. */
    public MyHashSet() {
        this.shelf = new BSTNode[initialNum];
        eleNum = 1;
    }
    public int hash(int key) {
        return key % shelf.length;
    }
    public void rehash() {
        BSTNode[] newShelf = new BSTNode[shelf.length * 2];
        BSTNode[] oldShelf = this.shelf;
        this.shelf = newShelf;
        for(BSTNode node:oldShelf) {
            if(node != null) {
                LinkedList<BSTNode> nodeList = node.linkedBSTNodes();
                ListIterator it = nodeList.listIterator();
                while(it.hasNext()) {
                    BSTNode linkedNode = (BSTNode)it.next();
                    add(linkedNode.data);
                }
            }
        }
    }
    public void add(int key) {
        BSTNode node = new BSTNode(key);
        int pos = hash(key);
        if(shelf[pos] != null) {
            shelf[pos].add(node);
        }else {
            shelf[pos] = node;
        }
        eleNum++;
        if(eleNum > rehashRate * shelf.length) {
            rehash();
        }
    }
    public void remove(int key) {
        int pos = hash(key);
        if(shelf[pos] != null) {
            shelf[pos] = shelf[pos].remove(key);
            eleNum--;
        }
    }   
    /** Returns true if this set contains the specified element */
    public boolean contains(int key) {
        int pos = hash(key);
        if(shelf[pos] != null) {
            return shelf[pos].contains(key);
        }
        return false;
    }
    private class BSTNode {
        public BSTNode left;
        public BSTNode right;
        public int data;
        protected BSTNode(int data) {
            this.data = data;
        }
        protected void add(BSTNode node) {
            if(this.data < node.data) {
                if(this.right == null) {
                    this.right = node;
                }else {
                    this.right.add(node);
                }
            }else if(this.data > node.data) {
                if(this.left == null) {
                    this.left = node;
                }else {
                    this.left.add(node);
                }
            }
        }
        protected LinkedList<BSTNode> linkedBSTNodes() {
            Queue<BSTNode> qu = new LinkedList<>();
            LinkedList<BSTNode> nodeList = new LinkedList<>();
            qu.offer(this);
            while(!qu.isEmpty()) {
                BSTNode curNode = qu.poll();
                nodeList.add(curNode);
                if(curNode.left != null) qu.offer(curNode.left);
                if(curNode.right != null) qu.offer(curNode.right);
            }
            return nodeList;
        }
        protected BSTNode remove(int data) {
            if(this.data == data) {
                if(this.left == null && this.right == null) return null;
                if(this.left == null || this.right == null) return this.left == null?this.right:this.left;
                this.data = this.left.findMax().data;
                this.left.remove(this.data);
            }else if(data < this.data && this.left != null) {
                this.left = this.left.remove(data);
            }else if(data > this.data && this.right != null) {
                this.right = this.right.remove(data);
            }
            return this;
        }
        protected boolean contains(int data) {
            if(this.data == data) return true;
            if(data < this.data && this.left != null) {
                return this.left.contains(data);
            }else if(data > this.data && this.right != null) {
                return this.right.contains(data);
            }
            return false;
        }
        protected BSTNode findMax() {
            BSTNode tempNode = this;
            while(tempNode.right != null) {
                tempNode = tempNode.right;
            }
            return tempNode;
        }
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */
```

##2. Leetcode 706 (HashMap实现)

HashMap的实现：

- 数组+链表；
- 每一个链表的第一个节点是一个节点；
  - 每一个节点中具有value，key两个属性；
- 主要的函数是find

```java
class MyHashMap {
    public ListNode[] nodes = new ListNode[10000];
    /** Initialize your data structure here. */
    public MyHashMap() {
    }
    public int hash(int key) {
        return key % nodes.length;
    }
    /** value will always be non-negative. */
    public void put(int key, int value) {
        int pos = hash(key);
        if(nodes[pos] == null) {
            nodes[pos] = new ListNode(-1,-1);
        }
        ListNode findNode = find(nodes[pos],key);
        if(findNode.next != null) {
            findNode.next.value = value;
        }else {
            findNode.next = new ListNode(key,value);
        }
    }
    public ListNode find(ListNode ln,int key) {
        ListNode pre = null;
        ListNode node = ln;
        while(node != null && node.key != key) {
            pre = node;
            node = node.next;
        }
        return pre;
    }  
    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    public int get(int key) {
        int pos = hash(key);
        if(nodes[pos] == null) {
            return -1;
        }else {
            ListNode findNode = find(nodes[pos],key);
            return findNode.next == null?-1:findNode.next.value;
        }
    }
    
    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    public void remove(int key) {
        int pos = hash(key);
        if(nodes[pos] == null) return;
        ListNode findNode = find(nodes[pos],key);
        findNode.next = findNode.next == null?null:findNode.next.next;
        
    }
    private class ListNode {
        public int key;
        public int value;
        public ListNode next;
        public ListNode(int key,int value) {
            this.key = key;
            this.value = value;
        }
    }
}
/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */
```

# HashSet/HashMap应用

## 1. Leetcode 349

Given two arrays, write a function to compute their intersection.

**Example 1:**

```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
```

**Example 2:**

```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
```

找到两个数组的交集；

- 用HashMap存上一个；
- 遍历另一个如果在Map中存在的就放在set中；

```java
lass Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        HashMap<Integer,Integer> map = new HashMap<>();
        for(int num:nums1) {
            map.put(num,1);
        }
        int size = 0;
        Set<Integer> res = new HashSet<>();
        for(int num:nums2) {
            if(map.containsKey(num)) {
                res.add(num);
            }
        }
        int[] r = new int[res.size()];
        int i = 0;
        for(int num:res) {
            r[i++] = num;
        }
        return r;
    }
}
```

## 2. Leetcode 202

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

**Example:** 

```
Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
```

找到一个快乐数，就是将每一位的数字平方和相加的到一个数N，将这个数字N也做相同的操作，如果这些和中出现 1 ，那么就说这是一个快乐数，如果循环了但还没有1出现说明不是快乐数字；

- 计算每次的平方和并且将结果存入hashmap中；
- 出现循环停止；
- 出现1停止；

```java
class Solution {
    public boolean isHappy(int n) {
        HashMap<Integer,Integer> map = new HashMap<>();
        while(!map.containsKey(n)) {
            map.put(n,1);
            n = cal(n);
            if(n == 1) {
                return true;
            }
        }
        return false;
    }
    public int cal(int n) {
        int res = 0;
        while(n != 0) {
            int temp = n % 10;
            n /= 10; 
            res += temp*temp;
        }
        return res;
    }
}
```

## 3. Leetcode 205

Given two strings **s** and **t**, determine if they are isomorphic.

Two strings are isomorphic if the characters in **s** can be replaced to get **t**.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

**Example 1:**

```
Input: s = "egg", t = "add"
Output: true
```

**Example 2:**

```
Input: s = "foo", t = "bar"
Output: false
```

这道题的意思就是两个字符串是不是同构的：

- 每一个在s中出现的字符有唯一的对应；
- 每一个在t中出现的字符有唯一的对应；

满足着两个条件就是"同构”的；

- 在s，t中分别构造一个 HashMap ，存储s，t中的对应，遍历两个字符串中的元素，判断在每一个元素是不是唯一对应的，如果这个s/t中的元素存在但是对应的不是之前对应的，那么就说明不是同构的；

```java
class Solution {
    public boolean isIsomorphic(String s, String t) {
        HashMap<Character,Character> map1 = new HashMap<>();
        HashMap<Character,Character> map2 = new HashMap<>();
        int size = s.length();
        for(int i = 0;i < size;i++) {
            if(!map1.containsKey(s.charAt(i))) {
                map1.put(s.charAt(i),t.charAt(i));
            }
            if(!map2.containsKey(t.charAt(i))) {
                map2.put(t.charAt(i),s.charAt(i));
            }
            if(map1.get(s.charAt(i)) != t.charAt(i) || 
              map2.get(t.charAt(i)) != s.charAt(i)) {
                return false;
            }
        }
        return true;
    }
}
```

第二种思路和第一个思路其实很相似，因为对应元素都是同时出现的，所以每一次出现的时候在 s 中的这个元素对应的位置和其在t 中对应元素应该是相同的，并且每一次 s 的这个元素出现那么 t 中的这个元素也必须出现；

- s 和 t 中的对应元素是同时出现的；
  - 每一次出现A就必须出现B，所以每次出现更新标记为其出现的位置；
  - 如果其中一个元素单独导致上次出现的位置不同导致不是同构；

```java
class Solution {
    public boolean isIsomorphic(String s, String t) {
        int[] m = new int[512];
        for(int i = 0;i < s.length();i++) {
            if(m[s.charAt(i)] != m[t.charAt(i) + 256]) return false;
            m[s.charAt(i)] = m[t.charAt(i) + 256] = i+1;
        }
        return true;
    }
}
```

## 4. Leetcode 599

Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings. 

You need to help them find out their **common interest** with the **least list index sum**. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

**Example 1:**

```
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
```

找到两个人最喜欢的几个餐馆，两个人分别将自己喜欢的餐馆按照喜欢的程度排序列出来：

- 所以一个餐馆在两个人的列表的 index 之和是判断其是否作为结果的依据；

利用 HashMap 首先将一个人的喜欢的餐馆的名字和 index 存入：

- 遍历另外一个人的列表之后，如果存在都喜欢的餐馆，判断当前的餐馆在两个人的列表中的 index 之和是不是小于当前的餐馆的index之和俄最小数值；
  - 如果是最小数值那么重新填入 res 并计数；
  - 如果相同那么继续填入 res；

```java
lass Solution {
    public String[] findRestaurant(String[] list1, String[] list2) {
        HashMap<String,Integer> m = new HashMap<>();
        int count = 0;
        for(String str:list1) {
            m.put(str,count++);
        }
        count = 0;
        int min = Integer.MAX_VALUE;
        String[] res = new String[list1.length];
        int number = 0;
        for(String str:list2) {
            if(m.containsKey(str)) {
                if(min >= m.get(str) + count) {
                    if(min > m.get(str) + count) {
                        number = 0;
                        min = m.get(str) + count;
                    }
                    res[number++] = str;
                }
            }
            count++;
        }
        return Arrays.copyOfRange(res,0,number);
    }
}
```

## 5. Leetcode 49

Given an array of strings, group anagrams together.

**Example:**

```
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```

把含有相同字符的字符串放在一起：

- 首先把每一个出现的字符串变成字符数组，排序，含有相同的字符的排序之后都是一样的，放在HashMap中；

```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String,List<String>> res = new HashMap<>();
        for(String str:strs) {
            char[] temp = str.toCharArray();
            Arrays.sort(temp);
            String newStr = String.valueOf(temp);
            if(res.containsKey(newStr)) {
                res.get(newStr).add(str);
            }else {
                List<String> strlist = new ArrayList<>();
                strlist.add(str);
                res.put(newStr,strlist);
            }
        }
        return new ArrayList<List<String>>(res.values());
    }
}
```

## 6. Leetcode 36

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated **according to the following rules**:

1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the 9 `3x3` sub-boxes of the grid must contain the digits `1-9` without repetition.

![img](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)

这是一个数独的问题，满足下面三个条件才能返回 True：

- 每一行都必须是 1-9 的数字，不能有重复；
- 每一列也必须是 1-9 的数字，不能有重复；
- 每一个小的 3*3 的方格也必须是 1-9 的数字不能重复；

所以就是要判断在遍历每一个点的时候每一个条件是不是符合：

- 在每一行的遍历的时候利用一个数组就可以解决，将遍历到的数值作为index放进nums[index ] = 1；如果在这一行遍历的过程中发生重复的数值就返回false；
- 在每一列的遍历需要一个 HashMap 将每一列对应一个数组，遍历到这列的时候如果存在重复返回false；
- 在每一个小的 3*3 的方格中需要重新定义坐标：
  - 定义一个loc\[3][3]的数组并将遍历的到的数值的坐标转换为对应的小方格的坐标，小方格的标号为1-9；
  - 遍历到的坐标—>小方格的坐标—>小方格的编号—>对应的 HashMap 中的数组；

```java
class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashMap<Integer,int[]> map = new HashMap<>();
        int[][] loc = new int[3][3];
        int count = 0;
        for(int i = 0;i < 3;i++) {
            for(int j = 0;j < 3;j++) {
                loc[i][j] = count++;
            }
        }
        HashMap<Integer,int[]> map2 = new HashMap<>();
        for(int i = 0;i < 9;i++) {
            int[] nums = new int[9];
            for(int j = 0;j < 9;j++) {
                if(board[i][j] == '.') {
                    continue;
                }
                int pos = board[i][j] - '0' - 1;
                int bigI = i / 3;
                int bigJ = j / 3;
                if(!map2.containsKey(loc[bigI][bigJ])) {
                    int[] temp = new int[9];
                    temp[pos] = 1;
                    map2.put(loc[bigI][bigJ],temp);
                }else {
                    if(map2.get(loc[bigI][bigJ])[pos] == 1) {
                       return false;
                    }else {
                        int[] a = map2.get(loc[bigI][bigJ]);
                        a[pos] = 1;
                        map2.put(loc[bigI][bigJ],a);
                    }
                }
                if(!map.containsKey(j)) {
                    int[] tempNums = new int[9];
                    tempNums[pos] = 1;
                    map.put(j,tempNums);
                }else {
                    if(map.get(j)[pos] == 1) {
                        return false;
                    }else {
                        int[] temp = map.get(j);
                        temp[pos] = 1;
                        map.put(j,temp);
                    }
                }
                if(nums[pos] == 1) return false;
                nums[pos] = 1;
            }
        }
        return true;
    }
}
```

