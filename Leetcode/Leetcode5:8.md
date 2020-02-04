[TOC]

# Leetcode 7

Given a 32-bit signed integer, reverse digits of an integer.

**Example 1:**

```
Input: 123
Output: 321
```

**Example 2:**

```
Input: -123
Output: -321
```

**Example 3:**

```
Input: 120
Output: 21
```

很简单的题，从最小的位数放进一个数组里面，主要是注意结果是最大整数或者最小的整数情况；

```java
class Solution {
    public int reverse(int x) {
        ArrayList<Integer> a = new ArrayList<>();
        while(x != 0) {
            int temp = x % 10;
            a.add(temp);
            x /= 10;
        }
        int count = a.size() - 1;
        int res = 0;
        for(int num:a) {
            res += num*Math.pow(10,count--);
        }
        return res == Integer.MAX_VALUE || res == Integer.MIN_VALUE?0:res; 
    }
}
```

# Leetcode 8

Implement `atoi` which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

**Note:**

- Only the space character `' '` is considered as whitespace character.
- Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

**Example 1:**

```
Input: "42"
Output: 42
```

**Example 2:**

```
Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
```

题很长，主要就是要注意规则：

- 如果出现了一个符号就决定了这个数是正的还是负的；
- 如果出现了多个字符不是数字，就返回0；
- 如果出现的是空字符在出现的数字之前是可以的；
- 当出现的数字过大大于了整数的最大数值的时候要注意判断，当前的符号是什么

```java
class Solution {
    public int myAtoi(String str) {
        int res = 0;
        int count = 0;
        boolean start = false;
        int sign = 1;
        for(char c:str.toCharArray()) {
            int newRes = 0;
            if(c >= '0' && c <= '9') {
                int a = c - '0';
                start = true;
                newRes = res * 10 + a;
                if(newRes < 0 || (newRes - a) / 10 != res) {
                    return sign >0?Integer.MAX_VALUE:Integer.MIN_VALUE;
                }
            }else if(c == '-' && !start) {
                sign = -1;
                start = true;
                continue;
            }else if(c == '+' && !start) {
                start = true;
            }else if(c == ' ' && !start){
                continue;
            }else {
                break;
            }
            res = newRes;
        }
        return sign == 1?res:-res;
    }
}
```

# Leetcode 9

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

**Example 1:**

```
Input: 121
Output: true
```

**Example 2:**

```
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

**Example 3:**

```
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

利用双端队列进行存储每一位；

```java
class Solution {
    public boolean isPalindrome(int x) {
        boolean sign = x >= 0;
        if(!sign) return false;
        Deque<Integer> dq = new LinkedList<>();
        int temp = 0;
        while(x != 0) {
            temp = x % 10;
            dq.addLast(temp);
            x = x / 10;
        }
        while(!dq.isEmpty()) {
            if(dq.getLast() == dq.getFirst()) {
                dq.pollFirst();
                dq.pollLast();
                continue;
            }else {
                return false;
            }
        }
        return true;
    }
}
```

