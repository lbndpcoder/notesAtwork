[TOC]

# 1. Leetcode 221（找最大区域）

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

**Example:**

```
Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
```

找到其中的最大的正方形的面积，正方形由"1"构成：

- 利用DP的思路，再构建一个数组用来存储DP数值；
  - 如果一个字符在a 中是1，那么这个数值的《左上角，上面，左面》的数值都应该是“1”，此时才可以组成一个正方形，否则那么这个位置的数值为0；
- 同理，如果一个位置的数值是2那么说明它周围的数值都是1，此时是一个边为2的正方形；

```
0 0 0 0 0 0
0 1 0 1 0 0
0 1 0 1 1 1
0 1 1 1 1 1
0 1 0 0 1 0
```

```java
class Solution {
    public int maximalSquare(char[][] matrix) {
        int r = matrix.length;
        if(r <= 0) {
            return 0;
        }
        int c = matrix[0].length;
        int res = 0;
        int[][] b = new int[r + 1][c + 1];
        for(int i = 1;i <= r;i++) {
            for(int j = 1;j <= c;j++) {
                if(matrix[i - 1][j - 1] == '1') {
                    b[i][j] = Math.min(Math.min(b[i - 1][j],b[i - 1][j - 1]),b[i][j - 1]) + 1;
                    res = Math.max(res,b[i][j]);
                }
            }
        }
        return res * res;
        
    }
}
```

# 2. Leetcode 764（找最大区域）

In a 2D `grid` from (0, 0) to (N-1, N-1), every cell contains a `1`, except those cells in the given list `mines` which are `0`. What is the largest axis-aligned plus sign of `1`s contained in the grid? Return the order of the plus sign. If there is none, return 0.

An "*axis-aligned plus sign of 1s* of order **k**" has some center `grid[x][y] = 1`along with 4 arms of length `k-1` going up, down, left, and right, and made of `1`s. This is demonstrated in the diagrams below. Note that there could be `0`s or `1`s beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1s.

**Examples of Axis-Aligned Plus Signs of Order k:**

```
Order 1:
000
010
000

Order 2:
00000
00100
01110
00100
00000

Order 3:
0000000
0001000
0001000
0111110
0001000
0001000
0000000
```

这个题的意思就是说给你一个N*N的矩阵，其中的元素是1或者0，其中0的位置通过mines数组告诉你，然后找到其中最大的由1组成的**十字形**。最初的想法就是在每一个点分别遍历上下左右找到其中的最小的数值作为探索的最远的距离，返回的数值是十字形的中心到任意的一个断点的距离；为了使得整体的时间复杂度变的更低，在每一个点的遍历都会分别更新：

- 所在行的每一个点的距离右侧的最远距离/距离左侧的最远距离；
  - 得到的是所在行的元素在左右能触及到的最远的距离；
- 所在列元素的距离下方的距离；
- 所在对角线的距离上方的距离；
- 当遇到 mines 中的"0"的时候我们知道相当于一个边界，直接在比较的上/下/左/右变为0；
- 其中的每次遍历的元素都是在变化，逐渐由当前返回的上下左右最大距离的最小距离更新；

最终可以得到的是这个点的在四个方向上最远距离并且进行比较的到的是在这个点可以得到的最大的十字星；

```java
class Solution {
    public int orderOfLargestPlusSign(int N, int[][] mines) {
        int[][] g = new int[N][N];
        for(int i = 0;i < N;i++) {
            Arrays.fill(g[i],N);
        }
        for(int[] mine:mines) {
            g[mine[0]][mine[1]] = 0;
        }
        for(int i = 0;i < N;i++) {
            for(int j = 0,k = N - 1,l = 0,r = 0,u = 0,d = 0;j < N;k--,j++) {
                g[i][j] = Math.min(g[i][j],l = g[i][j] == 0?0:(l + 1));
                g[i][k] = Math.min(g[i][k],r = g[i][k] == 0?0:(r + 1));
                g[j][i] = Math.min(g[j][i],u = g[j][i] == 0?0:(u + 1));
                g[k][i] = Math.min(g[k][i],d = g[k][i] == 0?0:(d + 1));
            }
        }
        int res = 0;
        for(int i = 0;i < N;i++) {
            for(int j = 0;j < N;j++) {
                res = Math.max(res,g[i][j]);
            }
        }
        return res;
    }
}
```

# 3. Leetcode 1021（关于括号）

A valid parentheses string is either empty `("")`, `"(" + A + ")"`, or `A + B`, where `A` and `B` are valid parentheses strings, and `+` represents string concatenation.  For example, `""`, `"()"`, `"(())()"`, and `"(()(()))"` are all valid parentheses strings.

A valid parentheses string `S` is **primitive** if it is nonempty, and there does not exist a way to split it into `S = A+B`, with `A` and `B` nonempty valid parentheses strings.

Given a valid parentheses string `S`, consider its primitive decomposition: `S = P_1 + P_2 + ... + P_k`, where `P_i` are primitive valid parentheses strings.

Return `S` after removing the outermost parentheses of every primitive string in the primitive decomposition of `S`.

**Example 1:**

```
Input: "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
```

**Example 2:**

```
Input: "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
```

将所有的括号去掉一层的到下一层的所有的"（）"；

- 如果遇到第一个"（ "那么，证明此时存在一个等待去掉的外层，此时opened += 1；
  - 如果下一层碰见一个" ）"说明已经找到删掉的那一层 opened -= 1；
  - 如果碰见的是"（"说明此时的是内部的括号，可以添加到res中；
- 只要在外层的opened > 1就说明此时外层有一个括号，就说明此时碰见的内部任意括号都可以添加；
  - 并且每一次遇见一个"）"都会削弱opened的数值；

```java
class Solution {
    public String removeOuterParentheses(String S) {
        StringBuffer res = new StringBuffer();
        int size = S.length();
        int opened = 0;
        int i = 0;
        for(char c:S.toCharArray()) {
            if(c == '(' && (opened++) > 0) res.append('(');
            if(c == ')' && (opened--) > 1) res.append(')');
        }
        return res.toString();
    }
}
```

