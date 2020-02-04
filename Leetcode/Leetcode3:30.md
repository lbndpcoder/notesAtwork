[TOC]

#1. Leetcode 210 (Course Schedule II：graph)

There are a total of *n* courses you have to take, labeled from `0` to `n-1`.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: `[0,1]`

Given the total number of courses and a list of prerequisite **pairs**, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

**Example 1:**

```
Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .
```

是 207 的一个进化版本的题。区别是在这道题中需要输出学习的顺序序列，有一些课程是需要多个课程为预备课程的，首先说一下需要的信息（数据结构）：

- 需要一个临接表（ adj ）用来表示每一个课程学完之后可以学习哪一些课程；
  - 2—>(1,3,4) / 1—>(4,5)；
- 需要一个保存"入度”的数组用来保证每一个课程所有的预备课程都学完了才可以被学习；
- 实现 BFS 的搜索需要的队列；
- 一个用来存储结果的 res 数组和记录实现学习的次数的count；

首先利用 prerequisites 来创建一个 adj，然后只要出现一个课程需要提前学习别的课程就更新 in 来创建入度的数组，将不需要预备课程的课程首先入队（如果没有的话就说明出现环了！说明无法学习！返回 [0] ）入队之后，弹出队列的第一个元素，加入 res 中意味着这个课程不需要学习别的课程就能学习了所以可以加入（其实在加入队列的时候就知道了）然后遍历以这个课程为预备课程的所有课程，将找到的课程入度 -1，如果入度为0，加入队列当中；

```java
class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        int size = numCourses;
        ArrayList[] adj = new ArrayList[size];
        int[] in = new int[size];
        for(int i = 0;i < size;i++) {
            adj[i] = new ArrayList();
        }
        for(int i = 0;i < prerequisites.length;i++) {
            adj[prerequisites[i][1]].add(prerequisites[i][0]);
            in[prerequisites[i][0]] += 1;
        }
        int[] res = new int[size];
        Queue<Integer> qu = new LinkedList();
        for(int i = 0;i < size;i++) {
            if(in[i] == 0) {
                qu.offer(i);
            }
        }
        int count = 0;
        while(!qu.isEmpty()) {
            int temp = qu.poll();
            res[count++] = temp;
            for(int i = 0;i < adj[temp].size();i++) {
                in[(int)adj[temp].get(i)] -= 1;
                if(in[(int)adj[temp].get(i)] == 0) {
                    qu.offer((int)adj[temp].get(i));
                }
            }
        }
        return res.length == count?res:new int[0];
    }
}
```

#2. Leetcode 721（DFS：graph**）

Given a list `accounts`, each element `accounts[i]` is a list of strings, where the first element `accounts[i][0]` is a *name*, and the rest of the elements are *emails*representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails **in sorted order**. The accounts themselves can be returned in any order.

**Example 1:**

```
Input: 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation: 
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
```

题目很长，大概说一下：

- 每一个人名字下面会有很多的邮箱地址；
- 但是可能一个人会出现多次，那么就会有很多的记录这个人的邮箱；
- 但是还会有重名的，如何判断两个重名的是否是一个人，通过邮箱判断，如果两个人是一个人一定会有重名的邮箱；
- 所以就是在给定的记录下找到所有人的所有邮箱；

大概的思路也是利用图的 DFS ：

- 首先建立 graph，graph 中是每一个邮箱和邮箱之间的关联利用的是map；
- 在建立 graph 的同时建立邮箱和 name 的对应；
- 利用 DFS 对有关系的邮箱进行搜索，因为只要**出现在一起的邮箱一定是一个人的邮箱**；

```java
class Solution {
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        Map<String,Set<String>> graph = new HashMap<>();
        Map<String,String> name = new HashMap<>();
        for(List<String> account:accounts) {
            String p = account.get(0);
            int size = account.size();
            for(int i = 1;i < size;i++) {
                String email = account.get(i);
                if(!graph.containsKey(email)) {
                    graph.put(email,new HashSet<>());
                }
                name.put(email,p);
                if(i == 1) continue;
                graph.get(email).add(account.get(i - 1));
                graph.get(account.get(i - 1)).add(email);
            }
        }
        Set<String> visited = new HashSet<>();
      //利用的是linkedList在后面可以直接将 name 添加；
        List<List<String>> res = new LinkedList<>();
        for(String email:name.keySet()) {
            List<String> temp = new LinkedList<>();
            if(visited.add(email)) {
                dfs(graph,visited,email,temp);
                Collections.sort(temp);
                temp.add(0,name.get(email));
                res.add(temp);
            }
        }
        return res;
    }
    public void dfs(Map<String,Set<String>> graph,Set<String> visited,String email,List<String> temp) {
        temp.add(email);
        int size = graph.get(email).size();
        for(String next:graph.get(email)) {
            if(visited.add(next)) {
                dfs(graph,visited,next,temp);
            }
        }
    }
}
```

