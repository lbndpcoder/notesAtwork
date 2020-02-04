[TOC]

# 1. 找到重复数字（1）

- 长度是 n 的数组其中的元素是（ 0 到 n-1 ）；
- 找到其中的重复的元素；

其实建立一个hashtable就可以了，书中的解法是根据下标:

- 当前的下标为 0 ，所以当前下标的数值为 nums[0] ，找到和当前下标相同的元素进行替换，否则一直和当前数值作为下标的数值替换，或者发现当前数值和当前数值作为下标的数值相同，就发现重复数值；

```java
public class OfferOne {
    public int getDup(int[] nums) {
        int length = nums.length;
        for(int i = 0;i < length;i++) {
            while(nums[i] != i) {
                if(nums[i] == nums[nums[i]]) {
                    return nums[i];
                }else {
                    int temp = nums[i];
                    nums[i] = nums[nums[i]];
                    nums[temp] = temp;
                }
            }
        }
        return -1;
    }
}
```

# 2. 找到重复数字（2）

给定一个n+1长度的数组，那么其中的数值都是在 1 到 n 中，找到其中的重复的元素；

其实通用的解法就是hash但是。。。。书中给的是用二分查找的方法：

- 二分的是1 到 n 这个查找的范围；
- 在这个范围内如果出现的数字的个数大于这个范围那么就说明有重复的数字，继续在这个区间二分查找；
- 如果不在这个区间的话就换到另一个区间查找；

```java
public class OfferTwo {
    public int getDuplication(int[] nums,int length) {
        if(length < 1) {
            return -1;
        }
        int start = 1;
        int end = length - 1;
        while(start <= end) {
            int mid = ((end - start) >> 1) + start;
            int count = countNumber(nums,start,mid);
            if(start == end) {
                if(count > 1) {
                    return start;
                }else {
                    return -1;
                }
            }
            if(count > mid - start + 1) {
                end = mid;
            }else {
                start = mid + 1;
            }
        }
        return -1;
    }
    public int countNumber(int[] nums,int start,int end) {
        int count = 0;
        for(int i = 0;i < nums.length;i++) {
            if(nums[i] >= start && nums[i] <= end) {
                count++;
            }
        }
        return count;
    }
}
```

# 3. 二维数组中的查找

在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

主要是从右上角开始寻找，如果矩阵中的元素小于当前的元素那么column减去一列，如果矩阵元素小于target那么从下一行开始；始终寻找的是右上角的元素；

```java
public class Solution {
    public boolean Find(int target, int [][] array) {
        int row = array.length;
        int column = array[0].length;
        for(int i = 0;i < row;i++) {
            for(int j = column - 1;j >= 0;j--) {
                if(array[i][j] == target) {
                    return true;
                }else if(array[i][j] < target) {
                    break;
                }else {
                    continue;
                }
            }
        }
        return false;
    }
}
```

# 4. 替换空格

请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

主要就是 stringbuffer 的几个用法；

- setCharAt
- insert

```java
public class Solution {
    public String replaceSpace(StringBuffer str) {
    	int length = str.length();
      int i = 0;
        while(i < length) {
            if(str.charAt(i) == ' ') {
            		str.setCharAt(i,'0');
            		str.insert(i,'2');
                str.insert(i,'%');
                i += 3;
              	//每次增加新元素需要重新评估length；
                length = str.length();
            }else {
                i++;
            }
        }
        return str.toString();
    }
}
```

# 5. 从尾到头打印链表

输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

很简单。。。遍历一遍链表，利用的是 ArrayList 的

```java
add(int location, E object) 
```

```java
/*
*    public class ListNode {
*        int val;
*        ListNode next = null;
*
*        ListNode(int val) {
*            this.val = val;
*        }
*    }
*
*/
import java.util.ArrayList;
public class Solution {
    public ArrayList<Integer> printListFromTailToHead(ListNode listNode) {
        ArrayList<Integer> res = new ArrayList<>();
        while(listNode != null) {
            res.add(0,listNode.val);
            listNode = listNode.next;
        }
        return res;
    }
}
```

# 6. 根据前序中序构建二叉树

如题，主要的思路是根据前序找到在中序中的位置，然后确定左子树右子树分别在前序和中序中的位置；

- 前序当前的位置是 i ，那么处在位置 i 的数值是 pre[i] ,找到这个数值在in的位置，就可以确定左子树的节点的个数；
- 同时确定右子树的节点个数，划分范围；
- 每一层构建一个节点都是当前范围内的第一个前序中的数值;

```java
/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public TreeNode reConstructBinaryTree(int [] pre,int [] in) {
        int length = pre.length;
        TreeNode root = buildTree(pre,0,length - 1,in,0,length - 1);
        return root;
    }
    
    public TreeNode buildTree(int[] pre,int preStart,int preEnd,int[] inNew,int inStart,int inEnd) {
        if(preStart > preEnd || inStart > inEnd) {
            return null;
        }
        TreeNode curRoot = new TreeNode(pre[preStart]);
        for(int pos = inStart;pos <= inEnd;pos++) {
            if(pre[preStart] == inNew[pos]) {
                curRoot.left = buildTree(pre,preStart + 1,preStart + pos - inStart,inNew,inStart,pos - 1);
                curRoot.right = buildTree(pre,pos - inStart + preStart + 1,preEnd,inNew,pos + 1,inEnd);
                break;
            }
        }
        return curRoot;
    }
}
```

# 7.用两个栈实现队列

思路就是：

- 入栈的时候利用的是stack1；
- 出队列的时候，stack1—>stack2，stack2.pop()之后再从stack2回到stack1；

```java
import java.util.Stack;
public class Solution {
    Stack<Integer> stack1 = new Stack<Integer>();
    Stack<Integer> stack2 = new Stack<Integer>();
    
    public void push(int node) {
        stack1.push(node);
    } 
    public int pop() {
        while(!stack1.isEmpty()) {
            int node1 = stack1.pop();
            stack2.push(node1);
        }
        int node = stack2.pop();
        while(!stack2.isEmpty()) {
            int node2 = stack2.pop();
            stack1.push(node2);
        }
        return node;
    }
}
```

# 8. 旋转数组的最小数字

利用到旋转数组的特性：

- 旋转之后变成两个子数组；
  - 其中的一个数组的元素 >= 右侧的子数组，所以可以二分判断当前的点在一个数组，，如果在左侧的数组可以将查询的数组变小；
  - 特殊的是如果中间的大小和左侧的数值都是相同的情况此时只能逐个寻找；

```java
import java.util.ArrayList;
public class Solution {
    public int minNumberInRotateArray(int [] array) {
        int end = array.length - 1;
        int start = 0;
        while(start < end) {
            int last = start;
            int mid = (start + end) / 2;
            if(array[mid] > array[start]) {
                start = mid;
            }else {
                start++;
            }
            if(array[last] > array[start]) {
                break;
            }
        }
        return array[start];
    }
}
```

# 9. 斐波那契数列

1，1，2，3

```java
public class Solution {
    public int Fibonacci(int n) {
        return helper(n);
    }
    public int helper(int n) {
        if(n == 0) {
            return 0;
        }
        if(n == 1) {
            return 1;
        }
        if(n == 2) {
            return 1;
        }
        int res = helper(n - 1) + helper(n - 2);
        return res;
    }
}
```

非递归：

```java
public class Solution {
    public int Fibonacci(int n) {
        if(n == 0) {
            return 0;
        }
        if(n == 1) {
            return 1;
        }
        int res = 1;
        int last = 0;
        for(int i = 2;i <= n;i++) {
            int temp = res;
            res = res + last;
            last = temp;
        }
        return res;
    }
}
```



# 10. 跳台阶

一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

还算是比较经典的题型，和斐波那契数列比较类似；

- 在每一个台阶上可以是前一个台阶跳一步；
- 或者前一个的前一个跳两个；
- 所以dp[i] = dp[i - 1] + dp[i - 2];

```java
public class Solution {
    public int JumpFloor(int target) {
        int[] dp = new int[target + 1];
        if(target == 0){
            return 0;
        }
        dp[0] = 1;
        dp[1] = 1;
        for(int i = 2;i <= target;i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[target];
    }
}
```

# 11. 变态版跳台阶

一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

根据计算可以得到：
$$
f(n) = f(n - 1) + f(n - 2) + \dots + f(1) + 1 \\
f(n - 1) = f(n - 2) +\dots + 1 \\
f(n) = 2*f(n-1)
$$

```java
public class Solution {
    public int JumpFloorII(int target) {
        int[] a = new int[target + 1];
        a[0] = 1;
        a[1] = 1;
        if(target < 2) {
            return a[target];
        }
        for(int i = 2;i <= target;i++) {
            a[i] = 2 * a[i - 1];
        }
        return a[target];    
    }
}
```

# 12. 矩形覆盖

我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

找规律还是斐波那契数列；

```java
public class Solution {
    public int RectCover(int target) {
        if(target <= 0) {
            return 0;
        }
        int[] a = new int[target + 2];
        a[1] = 1;
        a[2] = 2;
        for(int i = 3;i <= target;i++) {
            a[i] = a[i - 1] + a[i - 2];
        }
        return a[target];
    }
}
```

# 13. 二进制中1的个数（*）

这道题的解法很巧妙，主要是利用：

- 二进制数字减 1 之后会把最右侧出现的 1 变成 0；
- 通过不断的循环改变右侧的1为0，从而当整个二进制为0之后停止循环；
- 比如最小的负数-1之后变成0；

```java
public class Solution {
    public int NumberOf1(int n) {
        int count = 0;
        while(n != 0) {
            count++;
            n = (n - 1) & n;
        }
        return count;
    }
}
```

# 14. 数值的整数次方（*）

其实就是实现pow这个函数；

- 注意的要点是底数为“0”的时候在指数"<0“要注意；
- 在指数为负数的时候要注意变成正数计算，在取得倒数；
- 注意利用公式: 

$$
a^{n} = \begin{cases}a^{n/2}*a^{n/2}&{n为偶数}\\ a^{(n-1)/2}*a^{(n-1)/2}&{n为奇数}\end{cases}
$$

利用这个公式可以实现高效的计算；

- 并且利用 " >> " 移位运算符表示 除2；
- 利用 "&"表示求余数；

```java
public class Solution {
    public double Power(double base, int exponent) {
        if(base == 0 && exponent < 0) {
            return 0;
        }
        if(exponent == 0) {
            return 1;
        }
        int flag = 0;
        if(exponent < 0) {
            flag = 1;
            exponent = -exponent;
        }
        double res = helper(base,exponent);
        return flag == 1?1/res:res;
    }
    public double helper(double base,int ex) {
        if(ex == 0) {
            return 1;
        }
        if(ex == 1) {
            return base;
        }
        double res = helper(base,ex >> 1);
        res *= res;
      //判断是不是奇数；
        if((ex & 1) == 1) {
            res *= base;
        }
        return res;
    } 
}
```

