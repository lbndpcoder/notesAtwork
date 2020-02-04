[TOC]

# 1. Leetcode 978（DP）

A subarray `A[i], A[i+1], ..., A[j]` of `A` is said to be *turbulent* if and only if:

- For `i <= k < j`, `A[k] > A[k+1]` when `k` is odd, and `A[k] < A[k+1]` when `k` is even;
- **OR**, for `i <= k < j`, `A[k] > A[k+1]` when `k`is even, and `A[k] < A[k+1]` when `k` is odd.

That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

Return the **length** of a maximum size turbulent subarray of A.

提炼一下问题就是找到<><><><>或者><><><><><><这种的最长的子串。解决的方式首先是将整个数组的两个符号的大小提炼出来如果两个数字左边大就是>，可以变成1，如果两个数字右侧大，就是0，如果相等就是2，得到一个size-1大小的数组。之后只需要遍历整个抽象出来的数组找到前后的数字加和如果是1的话则代表有3个数字的子集，如果加和是0或者2的话则代表的是相同的符号所以最多只能有两个元素，如果其中的元素为2的话则代表数字相同那么此时的子集的个数为1.

所以整体的思路都是建立在如何区分是不是重复的元素，设立一个dup的数值用来在检查出没有重复数值的时候将子集最大元素个数更新。

- 将数组的大小关系提炼成为一个 n-1 的数组，如果相等就是2，">”就是 1 ，"<" 就是 0 ；
- 提炼之后进行比较：
  - 对全部相等的数组设置一个dup = 1，如果出现所有元素都没有将dup改变那么就说明所有元素相同那么返回1；
  - 至少的子串长度在没有重复的情况下是2，所以a =2；
  - 如果出现相加是1的情况说明是子串的一部分；

```java
class Solution {
    public int maxTurbulenceSize(int[] A) {
        int a = 2;int b = 0;//只有在出现重复数值的情况下才会小于2个元素
        int size = A.length;
        if(size == 0) {
            return 0;
        }
        if(size == 1) {
            return 1;
        }
        int[] flag = new int[size - 1];
        for(int i =1;i < size;i++) {
            if(A[i - 1] > A[i]) {
                flag[i - 1] = 1;
            }else if(A[i - 1] == A[i]) {
                flag[i - 1] = 2;
            }else {
                flag[i - 1] = 0;
            }
        }
        int dup = 1;//当为1的时候代表是有重复值的
        for(int i = 1;i < size - 1;i++) {
            if(flag[i] + flag[i - 1] == 1) {
                a++;
                dup = 0;
                b = Math.max(a,b);
            }else if(flag[i - 1] == 2){
                a = 2;
                continue;
            }
            else if(flag[i - 1] + flag[i] == 0 || flag[i - 1] + flag[i] == 2) {
                dup = 0;
                a = 2;
                b = Math.max(a,b);
            }
        }
        if(dup == 1) {
            return 1;
        }
        return b;
    }
}
```

# 2. Leetcode 91（Tree，回溯）

A message containing letters from `A-Z` is being encoded to numbers using the following mapping:

```
'A' -> 1
'B' -> 2
...
'Z' -> 26
```

Given a **non-empty** string containing only digits, determine the total number of ways to decode it.

**Example 1:**

```
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
```

就是说给一个字符串，都是数字，每一个字母对应一个数字，要找到所有的字母的组合。因为12这个数字可能是1和2也可能是12单独表示一个字母。

- 首先是将给定的**字符串转换成为数组**；

- 可以将整个问题理解为一个**树形的回溯问题**比如说abc，a/bc，a/b/c，ab/c 这三种情况，
- 但是主要的不满足条件的回溯是这个数字的组合比26大，或者在当前的节点数字为0。
- 还有一个比较重要的问题是在叶子结点的时候，就是判断出来走到了末尾的时候要注意最后的数值同样要判断是否为0；

```java
class Solution {
    public int res = 0;
    public int numDecodings(String s) {
        int size = s.length();
        int[] numbers = new int[size];
        int i = 0;
        for(char numberChar:s.toCharArray()) {
            numbers[i] = numberChar - '0';//转换成为int型的数组的数值减去0的ASCII码的数值；
            i++;
        }
        dfs(numbers,0);
        return res;
    }
    public void dfs(int[] numbers,int root) {
        //因为如果最后的是一个2位数那么不存在0的情况，
        //当最后一个数值恰好是叶子节点需要注意是不是0；
        if(root >= numbers.length - 1) {
            if(root == numbers.length - 1) {
                if(numbers[root] == 0) {
                    return;
                }else {
                    this.res++;
                    return;
                }
            }
            this.res++;
            return;
        }
        //判断当前的左孩子的数值是不是0，如果是0直接返回；
        int littleNumber = numbers[root];
        if(littleNumber == 0) {
            return;
        }
        dfs(numbers,root+1);
        int bigNumber = numbers[root]*10 + numbers[root+1];
        if(bigNumber <= 26) {
            dfs(numbers,root + 2);
        }
    }
}
```

# 3. Leetcode 39（Combination Sum 1）

Given a **set** of candidate numbers (`candidates`) **(without duplicates)** and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sums to `target`.

The **same** repeated number may be chosen from `candidates` unlimited number of times.

**Note:**

- All numbers (including `target`) will be positive integers.
- The solution set must not contain duplicate combinations

```
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
```

Combination Sum是很常见的题，利用递归回溯。出口就是在target<0或者target == 0的时候分别回溯到上一层或者添加到答案。**这道题是可以有重复的数值来组成最后的答案的**

```java
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List res = new ArrayList();//注意返回的是List
        List temp = new ArrayList();
        helper(candidates,target,0,res,temp);
        return res;
    }
    public void helper(int[] can,int target,int start,List res,List temp) {
        if(target < 0) {
            return;//出口1
        }
        if(target == 0) {
            res.add(new ArrayList<>(temp));//出口2达到目标
        }
        for(int i = start;i < can.length;i++) {
            target -= can[i];
            temp.add(can[i]);
            helper(can,target,i,res,temp);
            target+=can[i];
            temp.remove(temp.size() - 1);
        }
    }
}
```



#4. Leetcode 40（Combination Sum 2）

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sums to `target`.

Each number in `candidates` may only be used **once** in the combination.

**Note:**

- All numbers (including `target`) will be positive integers.
- The solution set must not contain duplicate combinations.

这道题和上一个combination Sum的区别在于这个题中每一个元素只能使用一次，所以并且在出现的数字中有重复，解决的关键点在于：

- 如果两个相同的数值会导致出现两次比如在target=8的时候[1,7]/[1,7]：如果出现这种情况的话，首先需要排序将所有相同的数值放在一起，如果这个数值已经作为**根节点**了那么后面相同的值都可以直接略过不再作为同一层的根结点。
- 在提升速度上可以在排序的基础上，提前观察如果在当前的这个节点时的target的数值<0那么直接回溯。

```java
class Solution {
    List<List<Integer>> res = new ArrayList<>();
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<Integer> temp = new ArrayList<>();
        Arrays.sort(candidates);
        helper(candidates,temp,0,target);
        return res;
    }

    public void helper(int[] can,List temp,int start,int target) {
        if(target < 0) {
            return;
        }
        if(target == 0) {
            res.add(new ArrayList<>(temp));
        }
        /*提升速度的步骤在排好序的基础上可以在这个节点上直接看到下面的
        遍历都是没有必要的*/
        if(start < can.length) {
            if(target - can[start] < 0) {
                return;
            }
        }
        for(int i = start;i < can.length;i++) {
            //和之前的关键不同，在同一层跳过相同的数值的点
            if(i > start && can[i] == can[i - 1]) {
                continue;
            }
            temp.add(can[i]);
            helper(can,temp,i + 1,target - can[i]);
            temp.remove(temp.size() - 1);
        }
    }
}
```

# 5.Leetcode 216 (Combination Sum 3)

Find all possible combinations of ***k*** numbers that add up to a number ***n***, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

**Note:**

- All numbers will be positive integers.
- The solution set must not contain duplicate combinations.

**Example 1:**

```
Input: k = 3, n = 7
Output: [[1,2,4]]
```

利用1到9的数字但是不能重复使用给定一个求和目标数值n和要求用到的数字的个数k返回的是所有的数字组合。本题的关键其实和之前很相似，就是给定了一个1到9的数组而已，并且出口要求是得到的组合长度有要求；

```java
class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> temp = new ArrayList<>();
        helper(res,1,temp,n,k);
        return res;
    }
    public void helper(List res,int start,List temp,int target,int k) {
        if(target == 0 && temp.size() == k) {
            res.add(new ArrayList<>(temp));
            return;
        }else if(target < 0 || temp.size() > k) {
            return;
        }else {
            for(int i = start;i <= 9;i++) {
                temp.add(i);
                helper(res,i+1,temp,target - i,k);
                temp.remove(temp.size() - 1);
            }
        }
    }
}
```

