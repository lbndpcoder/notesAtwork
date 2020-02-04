[TOC]

# 全排列/组合/子数组/子串

## 1. Leetcode 46

###1.1 元素互相交换

### 1.2 不互相交换

## 2. Leetcode 47

## 3. 剑指offer / 字符串的全排列（重复）

输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

```java
import java.util.*;
public class Solution {
    public ArrayList<String> Permutation(String str) {
        ArrayList<String> res = new ArrayList<>();
        char[] a = str.toCharArray();
        if(a.length < 1) {
            return res;
        }
        Arrays.sort(a);
        int[] vis = new int[a.length]; 
        String st = new String();
        helper(a,res,st,vis);
        return res;
    }
    public void helper(char[] c,ArrayList<String> res,String str,int[] vis) {
        if(str.length() == c.length) {
            res.add(str);
        }else {
            for(int i = 0;i < c.length;i++) {
                //带有重复的元素的判断；
              	if(vis[i] == 1 || i > 0 && c[i] == c[i - 1] && vis[i - 1] != 1) continue;
                String temp = String.valueOf(c[i]);
                str += temp;
                vis[i] = 1;
                helper(c,res,str,vis);
                vis[i] = 0;
                if(str.length() == 1) {
                    str  = "";
                }else {
                    str = str.substring(0,str.length() - 1);
                }
            }
        }
    }
}
```

## 4. Leetcode 78（subSets）

## 5. Leetcode 90（subSets）

