[TOC]

# 1. Leetcode 207（DFS：graph）

There are a total of *n* courses you have to take, labeled from `0` to `n-1`.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: `[0,1]`

Given the total number of courses and a list of prerequisite **pairs**, is it possible for you to finish all courses?

**Example 1:**

```
Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
```

还是一个关于图的问题，这里使用的是 DFS 的思路，每一个课程可能会有先修的课程，将所有课程修完之后可以再修的课程放在一起进行DFS，单条线路上如果出现已经修过的节点，就说明出现环不满足要求；

- 利用的是 ArrayList[] 每一个数组中的元素存储的是每一个课修完之后才可以修的课；
- 遍历所有的课程找到修完每一个课之后可以修的下一门课，并将这门课设值visited；
- 继续向下寻找修完这个课还可以修的课程；

```java
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        ArrayList[] gra = new ArrayList[numCourses];
        for(int i = 0;i < numCourses;i++) {
            gra[i] = new ArrayList();
        }
        for(int i = 0;i < prerequisites.length;i++) {
            gra[prerequisites[i][1]].add(prerequisites[i][0]);
        }
        int[] visited = new int[numCourses];
        for(int i = 0;i < numCourses;i++) {
            if(!dfs(gra,visited,i)) {
                return false;
            }
        }
        return true;
    }
    public boolean dfs(ArrayList[] gra,int[] visited,int course) {
        if(visited[course] == 1) {
            return false;
        }
        visited[course] = 1;
        for(int i = 0;i < gra[course].size();i++) {
            if(!dfs(gra,visited,(int)gra[course].get(i))) {
                return false;
            }
         }
        visited[course] = 0;
        return true;
    }
}
```

# 2 . Leetcode 23（Merge k Sorted Lists）

Merge *k* sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

**Example:**

```
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
```

整体的思路是利用小顶堆：

- 修改 PriorityQueue，比较node里面的 val ；
- 同时建立一条新的 list 用来储存结果；
- 将每一条链的当前头节点放入 优先队列当中，进行排序，然后最小的数值的节点在peek，出队；
- 出队的同时将当前的出队的节点下一个节点入队，队列默认进行排序；
  - 就是每一次队列中的都是当前所有元素的前K小的元素，利用队列进行排序，将最小的放入；

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
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists == null || lists.length == 0) {
            return null;
        }
      //PriorityQueue<ListNode> pq = new PriorityQueue<ListNode>(lists.length,(a,b)->a.val - b.val);JAVA 的新特性；
        PriorityQueue<ListNode> pq = new PriorityQueue<ListNode>(lists.length,new Comparator<ListNode>() {
            @Override
            public int compare(ListNode o1,ListNode o2) {
                if(o1.val == o2.val) {
                    return 0;
                }else if(o1.val < o2.val) {
                    return -1;
                }else {
                    return 1;
                }
            }
        });
        
        ListNode head = new ListNode(0);
        ListNode end = head;
        for(ListNode node:lists) {
            if(node != null)
                pq.add(node);
            
        }
        while(!pq.isEmpty()) {
            end.next = pq.poll();
            end = end.next;
            if(end.next != null) {
                pq.add(end.next);
            }
        }
        return head.next;
    }
}
```

