[TOC]

# Leetcode 19

Given a linked list, remove the *n*-th node from the end of list and return its head.

**Example:**

```
Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
```

只需要两个指针，这两个指针之间的差距为N就可以：

- 创造一个 fakeHead 头节点；
- curNode 的初始位置和head节点的相距为 N - 1；
- 当curNode 为最后一个节点的时候，此时的fakeHead 为 要删除的节点的上一个节点；

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode fakeHead = new ListNode(0);
        fakeHead.next = head;
        ListNode curNode = fakeHead;
        int count = 0;
        while((count++) < n) {
             curNode = curNode.next;
        }
        ListNode f = fakeHead;
        while(curNode.next != null) {
            f = f.next;
            curNode = curNode.next;
        }
        f.next = f.next.next;
        return fakeHead.next;
    }
}
```

#Leetcode 20

Given a string containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

**Example 1:**

```
Input: "()"
Output: true
```

**Example 2:**

```
Input: "()[]{}"
Output: true
```

**Example 3:**

```
Input: "(]"
Output: false
```

这是一个关于括号的问题，利用栈：

```java
class Solution {
    public boolean isValid(String s) {
        Stack<Character> st = new Stack<>();
        for(char c:s.toCharArray()) {
            if(!st.isEmpty() && (st.peek() == '(' && c == ')'
              || st.peek() == '{' && c == '}' 
              || st.peek() == '[' && c ==']' )) {
                st.pop();
            }else {
                st.push(c);
            }
        }
        return st.isEmpty();
        
    }
}
```

# Leetcode 22

# Leetcode 34



