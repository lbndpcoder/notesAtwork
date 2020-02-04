[TOC]

# 1. Leetcode 349（哈希）

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

很简单的题，为了利用 hash 思想抛砖引玉用的，主要是找两个数组的交集，利用的数据结构是 HashMap 和 HashSet：

- 利用 HashMap 将一个数组存储，其中的元素存在那么存储映射；
- 遍历另一个数组，找到存在的元素放入 HashSet 中；

最终的到结果；

```java
class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        HashMap<Integer,Integer> map = new HashMap<>();
        int size1 = nums1.length;
        for(int i = 0;i < size1;i++) {
            int key = nums1[i];
            if(map.containsKey(key)) {
                continue;
            }else {
                map.put(key,1);
            }
        }
        Set<Integer> res = new HashSet<>();
        for(int i = 0;i < nums2.length;i++) {
            int key = nums2[i];
            if(map.containsKey(key)) {
                res.add(key);
            }
        }
        int[] r = new int[res.size()];
        int i = 0;
        for(int a:res) {
            r[i++] = a;
        }
        return r;
    }
}
```

# 2. Leetcode 202（哈希）

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

# 3. Leetcode 205（哈希）

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

# 4. Leetcode 599（哈希）

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
class Solution {
    public String[] findRestaurant(String[] list1, String[] list2) {
        HashMap<String,Integer> m = new HashMap<>();
        int count = 0;
        int size = list1.length > list2.length?list1.length:list2.length; 
        for(String str:list1) {
            m.put(str,count++);
        }
        String[] res = new String[size];
        count = 0;
        int min = Integer.MAX_VALUE;
        int num = 0;
        for(String str:list2) {
            if(m.containsKey(str)) {
                if(min >= m.get(str) + count) {
                    if(min > m.get(str) + count) {
                        num = 0;
                    }
                    min = m.get(str) + count;
                    res[num++] = str;
                }
            }
            count++;
        }
        return Arrays.copyOfRange(res,0,num);
    }
}
```

注意其中的 Arrays.copyOfRange(res,0,num);的使用；