[TOC]

# 1. Leetcode 84（stack：同4:1的题目）

Given *n* non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

 

![img](https://assets.leetcode.com/uploads/2018/10/12/histogram.png)
Above is a histogram where width of each bar is 1, given height = `[2,1,5,6,2,3]`.

 

![img](https://assets.leetcode.com/uploads/2018/10/12/histogram_area.png)
The largest rectangle is shown in the shaded area, which has area = `10`unit.

 

**Example:**

```
Input: [2,1,5,6,2,3]
Output: 10
```

这道题的大概意思就是在给定的一个矩形上找到面积最大的大矩形；整体的思路还是利用栈来解决问题：

- 构建一个递增的 stack；
  - 当遍历的元素小于栈顶的元素的数值（ stack 中存储的是 index）的时候，说明如果从当前的遍历元素画"一条线”，就会用这个当前遍历元素的高度决定面积，此时进行“总结”之前的递增的那几个元素可能得到的面积，并且一直弹栈直到 stack的peek元素位置的数值小于当前遍历的元素；
- 就是不断的构建递增的序列在stack中然后不断的"总结”；
  - "总结“就是说在递增的矩形中由高的矩形开始不断组合出最大的面积；

```java
class Solution {
    public int largestRectangleArea(int[] heights) {
        int size = heights.length;
        int[] h = new int[size + 2];
        for(int i = 1;i <= size;i++) {
            h[i] = heights[i - 1];
        }
        Stack<Integer> st = new Stack<>();
        st.push(0);
        int res = 0;
        for(int i = 1;i < h.length;i++) {
            while(!st.isEmpty() && h[i] < h[st.peek()]) {
                int curIndex = st.pop();
                res = Math.max(res,(i - st.peek() - 1)*h[curIndex]);
            }
            st.push(i);
        }
        return res;
    }
}
```

在代码中看见，构造了一个 n+2 长度的 h 数组，目的是保证最后的入栈元素为0是最小的，这样可以对整个序列进行最后的总结，并且第一个元素也是0，保证可以总结到序列的开头；

# 2. Leetcode 42（stack）

Given *n* non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

![img](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)
The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. **Thanks Marcos** for contributing this image!

**Example:**

```
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```

还是利用的 stack：

- 遍历每一个元素；
  - 如果当前的元素大于栈顶的元素，那么弹出栈；如果遇到比栈顶元素还要大的元素，说明这个时候可能遇到了右侧"边界”，就是右侧可以阻挡来存储雨水；
  - 此时栈顶的元素和右侧边界比较，较小的高度A（因为存储雨水是按照最低的高度来存储的）和弹出栈的元素做差（表示只计算高于弹出栈的高度和A之差的之间的高度可以存储的水量）；这里有一个特殊情况就是如果是负数则代表这层正常是可以存水的，但是有一个东西挡住了所以是负数；
  - 依次这么计算，栈顶元素相当于左边界（弹栈之后的栈顶元素），弹出栈的元素相当于告诉我们这个高度以下的已经计算好了，只需要计算这层上面的就可以了；

```java
class Solution {
    public int trap(int[] height) {
        int size = height.length;
        Stack<Integer> st = new Stack<>();
        int res = 0;
        for(int i = 0;i < size;i++) {
            while(!st.isEmpty() && height[st.peek()] < height[i]) {
                int curIndex = st.pop();
                if(st.isEmpty()) break;
                res += (Math.min(height[st.peek()],height[i]) - height[curIndex]) * (i - st.peek() - 1);
            }
            st.push(i);
        }
        return res;
    }
}
```

