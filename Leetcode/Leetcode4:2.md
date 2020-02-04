[TOC]

# 1. Leetcode 863（树图转换/图的BFS）

We are given a binary tree (with root node `root`), a `target` node, and an integer value `K`.

Return a list of the values of all nodes that have a distance `K` from the `target` node.  The answer can be returned in any order.

**Example 1:**

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.
```

```
Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
```

![sketch0](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/28/sketch0.png)

这道题是找到树中和某一个节点的距离为K的所有的节点的数值

- 将二叉树变成一个无向图；
  - 在根节点的孩子节点完成对图的构建；
  - 俩俩配对；
- 利用图的 BFS 每一层的搜索，知道搜索到第 K 层的时候将所有的节点的 val 放入其中；
  - 利用的是队列，遍历当前队列中的所有的元素，每一次出队列的都是上一层的元素，出去的元素将和和它相连的元素分别入队构成下一层；
  - 利用一个K值来查看层数，当 K == 0 的时候说明当前的层数是目标层数；

```java
class Solution {
    public HashMap<TreeNode,ArrayList<TreeNode>> map = new HashMap<>();
    public List<Integer> distanceK(TreeNode root, TreeNode target, int K) {
        List<Integer> res = new ArrayList<Integer>();
        if(root == null || K < 0) {
            return res;
        }
        buildGraph(root,null);
        Queue<TreeNode> qu = new LinkedList<>();
        Set<TreeNode> vis = new HashSet<>();
        qu.offer(target);
        vis.add(target);
        while(!qu.isEmpty()) {
            int size = qu.size();
            if(K == 0) {
                for(int i = 0;i < size;i++) {
                    res.add(qu.poll().val);
                }
                return res;
            }
            for(int i = 0;i < size;i++) {
                TreeNode node = qu.poll();
                for(TreeNode next:map.get(node)) {
                    if(vis.contains(next)) continue;
                    vis.add(next);
                    qu.offer(next);
                }
            }
            K--;
        }
        return res;
    }
    public void buildGraph(TreeNode node,TreeNode parent) {
        if(node == null) return ;
        if(!this.map.containsKey(node)) {
            map.put(node,new ArrayList());
            if(parent != null) {
                map.get(node).add(parent);
                map.get(parent).add(node);
            }
            buildGraph(node.left,node);
            buildGraph(node.right,node);
        }
    }
}
```

#2. Leetcode 310（树图转换/拓扑排序）

For an undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

**Format**
The graph contains `n` nodes which are labeled from `0` to `n - 1`. You will be given the number `n` and a list of undirected `edges` (each edge is a pair of labels).

You can assume that no duplicate edges will appear in `edges`. Since all edges are undirected, `[0, 1]` is the same as `[1, 0]` and thus will not appear together in `edges`.

**Example 1 :**

```
Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3 

Output: [1]
```

**Example 2 :**

```
Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5 

Output: [3, 4]
```

**Note**:

- According to the [definition of tree on Wikipedia](https://en.wikipedia.org/wiki/Tree_(graph_theory)): “a tree is an undirected graph in which any two vertices are connected by *exactly*one path. In other words, any connected graph without simple cycles is a tree.”
- The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

整个题就是找到树中的一些节点使得这些节点作为根的时候到叶子结点的最远距离最小：

- 首先将所有的两两相连的边变成图：

  - 图的结构是Arraylist和HashSet的组合；

- 然后将所有的叶子结点删掉，相当于最外层被删掉，一层一层的删掉最后剩下的一个或者两个节点就是要求的节点；

- 代码中的细节：

  - ```java
    Collections.singletonList(0)//减少内存的使用；
    ```

    ```java
    int next = adj.get(num).iterator().next();//返回一个迭代器之后取其中的第一个元素；
    ```

    

```java
class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        if(n == 1) {
            return Collections.singletonList(0);
        }
        List<Set<Integer>> adj = new ArrayList<>(n);
        for(int i = 0;i < n;i++) adj.add(new HashSet<>());
        for(int[] edg:edges) {
            adj.get(edg[0]).add(edg[1]);
            adj.get(edg[1]).add(edg[0]);
        }
        List<Integer> leaves = new ArrayList<>();
        for(int i = 0;i < n;i++) {
            if(adj.get(i).size() == 1) {
                leaves.add(i);
            }
        }
        while(n > 2) {
            n -= leaves.size();
            List<Integer> newLeaves = new ArrayList<>();
            for(int num:leaves) {
                int next = adj.get(num).iterator().next();
                adj.get(next).remove(num);
                if(adj.get(next).size() == 1) {
                    newLeaves.add(next);
                }
            }
            leaves = newLeaves;
        }
        return leaves;
    }
}
```

还有第二种的蠢方法。。。时间过不了。。但是毕竟自己敲的。。记录一下。。。

- 将真个edges变成图，map大法好；
- 利用 DFS 找到每一个点出发的最深路径；
- 找到最小的最深路径是哪几个点；
- 返回；

```java
class Solution {
    public HashMap<Integer,ArrayList<Integer>> map = new HashMap<>();
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        List<Integer> res = new ArrayList<>();
        if(n == 1) {
            res.add(0);
            return res;
        }
        for(int[] edg:edges) {
            for(int i = 0;i < 2;i++) {
                if(!map.containsKey(edg[i])) {
                    map.put(edg[i],new ArrayList());
                }
                map.get(edg[i]).add(i==1?edg[0]:edg[1]);
            }
        }
        int[] vis = new int[n];
        int[] path = new int[n];
        int last = n + 1;
        for(int num:map.keySet()) {
            int now = dfs(num,vis,0,0);
            if(now < last) {
                last = now;
                res.clear();
                res.add(num);
            }else if(now == last) {
                res.add(num);
            }
        }
        return res;
    }
    public int dfs(int num,int[] visited,int path,int deep) {
        if(visited[num] == 1) {
            return path;
        }
        visited[num] = 1;
        int size = map.get(num).size();
        for(int i = 0;i < size;i++) {
            int curLength = path;
            int temp = map.get(num).get(i);
            if(visited[temp] == 1)  {
                deep = Math.max(path,deep);
                continue;
            }
            path = dfs(temp,visited,path+1,deep);
            deep = Math.max(path,deep);
            path = curLength;
        }
        visited[num] = 0;
        return deep;
    }
}
```

