[TOC]

# Sliding window（2）

## 1. Leetcode 3（R）

## 2. Leetcode 219 （R）

##3. Leetcode 209（R）

##4. Leetcode 30

You are given a string, **s**, and a list of words, **words**, that are all of the same length. Find all starting indices of substring(s) in **s** that is a concatenation of each word in **words** exactly once and without any intervening characters.

**Example 1:**

```
Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
```

**Example 2:**

```
Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
```

# Leetcode 29

\29. Divide Two Integers

Medium

Given two integers `dividend` and `divisor`, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing `dividend` by `divisor`.

The integer division should truncate toward zero.

**Example 1:**

```
Input: dividend = 10, divisor = 3
Output: 3
```

**Example 2:**

```
Input: dividend = 7, divisor = -3
Output: -2
```

大整数除法：

- 都变成负数，不断的将除数扩大直到被除数大于除数的时候或者除数大于0的情况下break；
- 注意判断当被除数是整数的最小值的时候；

```java
class Solution {
    public int res = 0;
    public int divide(int A, int B) {
        if(A == Integer.MIN_VALUE && B == -1) return Integer.MAX_VALUE;
        boolean sign = A < 0 == B < 0;
        A = A < 0?A:-A;
        B = B < 0?B:-B;
        int res = div(A,B);
        return sign?res:-res;
    }
    public int div(int A,int B) {
        int res = 0;
        int total = B;
        int pre = 0;
        while(A <= total) {
            res = res == 0?res + 1:res + res;
            pre = total;
            total += total;
            if(total > pre) break;
        }
        return res == 0?res:res + div(A - pre,B);
    }
}
```

# ACWING

## 1. 678

##2. 679