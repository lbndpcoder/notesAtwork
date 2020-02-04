[TOC]

回文中最长见的解决方法就是利用两个指针判断：

- 5 / 125 / 680 / 234

在这个的基础上利用 DP 的思路有：

- 132

还有利用 HashMap 或者 其他的计算技巧：

- 866 / 409

利用 KMP 得到next [ ] 数组的思路：

- 214

**利用前缀树来解决** 的特别 ***酷*** 的思路：

- 336

# 5（*） 找到最长的回文子串

思路相当于是遍历，分别在字符串中的每一个字符向两边扩散，直到遇到边界或者两个指针所处的字符不相同了；需要注意的是每一次需要比较的是两种，即字符串是偶数个和字符串是奇数个；

```java
class Solution {
    public int max = 0;
    public int st = 0;
    public String longestPalindrome(String s) {
        if(s.length() < 2) return s;
        for(int i = 0;i < s.length();i++) {
            extendString(i,i,s);
            extendString(i,i + 1,s);
        }
        return s.substring(st,st + max);
    }
    public void extendString(int left,int right,String s) {
        while(left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        if(max < right - left - 1) {
            max = right - left - 1;
            st = left + 1;
        }
    }
}
```

# 132（*） 最少切割回文子串

一个字符串找到最少的切割次数，使得这些字符串都是回文的字符串；

- 出现回文子串的时候可以减少切割的次数；
  - 需要不断更新字符串在某一个范围是否回文；
  - 如果当前的字符 j 位置和 i 位置的字符相同，并且内部的字符是回文那么此时的切割次数变化；

```java
class Solution {
    public int minCut(String s) {
        int n = s.length();
        int[][] dp = new int[n][n];
        int[] cut = new int[n];
        int min = 0;
        for(int i = 0;i < n;i++) {
            min = i;
            for(int j = 0;j <= i;j++) {
                if(s.charAt(i) == s.charAt(j) && (j + 1 > i - 1 || dp[j + 1][i - 1] == 1)) {
                    dp[j][i] = 1;
                    min = j == 0?0:Math.min(min,cut[j - 1] + 1);
                    continue;
                }
            }
            cut[i] = min; 
        }
        return cut[n - 1];
    }
}
```

#125 判断是否回文

本题的重点在于判断字符串和数字，利用双指针；

- 判断如果不是数字也不是字符就下一个；$isLetterOrDigit$
- 忽略大小写；$toLowerCase$

重点在于会不会调包吧。。没什么意思。。

```java
class Solution {
    public boolean isPalindrome(String s) {
        int i = 0;
        int j = s.length() - 1;
        while(i < j) {
            while(!Character.isLetterOrDigit(s.charAt(i)) && i < j) {
                i++;
            }
            while(!Character.isLetterOrDigit(s.charAt(j)) && i < j) {
                j--;
            }
            if(Character.toLowerCase(s.charAt(i++)) != Character.toLowerCase(s.charAt(j--))) {
                return false;
            }
        }
        return true;
    }
}
```

# 409（*） 构建的回文子串的长度

思路：对对碰 over。

```java
class Solution {
    public int longestPalindrome(String s) {
        HashSet<Character> hs = new HashSet<>();
        int count = 0;
        for(char c:s.toCharArray()) {
            if(hs.contains(c)) {
                ++count;
                hs.remove(c);
            }else {
                hs.add(c);
            }
        }
        if(!hs.isEmpty()) return count * 2 + 1;
        return count * 2;
    }
}
```

# 866 判断是不是素数回文

给定一个数，大于这个数的最小的回文素数；

根据所有的素数回文，如果是偶数位那么一定会被11整除，所以，只考虑奇数位；

- 数字的范围是10^8，通过拼接只需要遍历一半的数字；
- 判断是不是大于N，并且是不是素数；
- 在判断素数的时候所有偶数只有 2 是素数；

```java
class Solution {
    public int primePalindrome(int N) {
        if(8 <= N && N <= 11) return 11;
        for(int x = 1;x < 100000;x++) {
            String s = Integer.toString(x);
            String r = new StringBuilder(s).reverse().toString().substring(1);
            int res = Integer.parseInt(s + r);
            if(res >= N && isPrime(res)) return res;
        }
        return -1;
    }
    public boolean isPrime(int x) {
        if(x < 2 || x % 2 == 0) return x == 2;
        for(int i = 3;i * i <= x;i += 2) {
            if(x % i == 0) return false;
        }
        return true;
    }
}
```

# 214（*） 补全字符串使得变成最短回文

KMP 中 next[] 数组的最后一个元素就是代表着前后最长相同的子串的长度是多长（在整个字符串中的位置）；

- 构建一个字符串：由给定的字符串s + "#"（分隔符）+reverse(s)；
- 利用 next[] 数组找到前后相同的部分，由于构造后的字符串的后半部分是反转的，其实就是可以理解成为找到最长的回文子串；
- 找到之后只需要在原来的 s 前面添加剩余非回文的部分就好了；

```java
class Solution {
    public String shortestPalindrome(String s) {
        String temp = s + "#" + new StringBuilder(s).reverse().toString();
        int[] table = next(temp);
        return new StringBuilder(s.substring(table[table.length - 1] + 1)).reverse().toString() + s;
    }
    
    public int[] next(String s) {
        int[] table = new int[s.length()];
        int i = -1;
        int j = 0;
        table[0] = -1;
        while(j < s.length() - 1) {
            if(i == -1 || s.charAt(i) == s.charAt(j)) {
                table[++j] = ++i; 
            }else {
                i = table[i];
            }
        }
        return table;
    }
}
```

# 680 最多删除一个字符能否成为回文

遍历一遍：

- 如果当前的字符不相同的话，那么就比较如果从左侧跳过一个，或者从右侧跳过一个是否剩下的是回文；

```java
class Solution {
    public boolean validPalindrome(String s) {
        int left = -1;int right = s.length();
        while(++left < --right) {
            if(s.charAt(left) != s.charAt(right)) {
                return pa(left-1,right,s) || pa(left,right+1,s);
            }
        }
        return true;
    }
    public boolean pa(int left,int right,String s) {
        while(++left < --right) {
            if(s.charAt(left) != s.charAt(right)) return false;
        }
        return true;
    }
}
```

# 234（*） 判断链表是不是回文

通过利用快慢指针:

- 快的指针跳两次，慢的跳一次；
- 慢的之后的反转；
- 然后进行比较；

```java
class Solution {
    public boolean isPalindrome(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        while(fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        if(fast != null) {
            slow = slow.next;
        }
        slow = reverse(slow);
        fast = head;
        while(slow != null) {
            if(slow.val != fast.val) {
                return false;
            }
            slow = slow.next;
            fast = fast.next;
        }
        return true;
    }
    public ListNode reverse(ListNode node) {
        ListNode pre = null;
        while(node != null) {
            ListNode n = node.next;
            node.next = pre;
            pre = node;
            node = n;
        }
        return pre;
    }
}
```

# 336（**）拼接成为回文字符串

问题：给定一个字符串的数组，找出所有的拼接可能使得成为回文；

整体思路的大概描述：

- 将字符串倒叙放入 Trie 的结构当中；
  - 在放入的时候每一个节点需要三个信息，
    - index：在字符串中的位置；
    - list：从根节点到当前节点是一个字符串，这个 list 保存的是包含这个字符串并且剩下的是回文的字符串的index；
    - next：代表的是一个数组，包含当前节点的子节点；
- 放入到 Trie 的结构当中，遍历每一个字符串：
  - 因为是倒序放入的，但是在查找的时候应该是按照字符串的正常顺序查找，这样找到的字符串就是可以拼在后面形成回文的字符串；
  - 因为之前存储了剩下的部分是不是回文的 list ，所以在拼接上将剩下的部分也是回文的也可以拼接上；

```java
class Solution {
    public static class TrieNode {
        public int index;
        public List<Integer> list;
        public TrieNode[] next;
        public TrieNode() {
            this.index = -1;
            this.list = new ArrayList<>();
            next = new TrieNode[26];
        }
    }
    public void add(String word,int index,TrieNode node) {
        for(int i = word.length() - 1;i >= 0;i--) {
            int j = word.charAt(i) - 'a';
            if(node.next[j] == null) node.next[j] = new TrieNode();
            if(isp(0,i,word)) node.list.add(index);
            node = node.next[j];
        }
        node.list.add(index);
        node.index = index;
    }
    public void search(List<List<Integer>> res,String word,int index,TrieNode root) {
        for(int i = 0;i < word.length();i++) {
            if(root.index >= 0 && root.index != index && isp(i,word.length() - 1,word)) {
                res.add(Arrays.asList(index,root.index));
            }
            int j = word.charAt(i) - 'a';
            root = root.next[j];
            if(root == null) return;
        }
        for(int j:root.list) {
            if(index == j) continue;
            res.add(Arrays.asList(index,j));
        }
    }
    public boolean isp(int i,int j,String str) {
        while(i < j) {
            if(str.charAt(i++) != str.charAt(j--)) return false;
        }
        return true;
    }
    public List<List<Integer>> palindromePairs(String[] words) {
        List<List<Integer>> res = new ArrayList<>();
        TrieNode node = new TrieNode();
        for(int i = 0;i < words.length;i++) add(words[i],i,node);
        for(int i = 0;i < words.length;i++) search(res,words[i],i,node);
        return res;
    }
}
```

