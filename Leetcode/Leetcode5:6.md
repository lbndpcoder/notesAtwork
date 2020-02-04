[TOC]

# Leetcode 1037

A *boomerang* is a set of 3 points that are all distinct and **not** in a straight line.

Given a list of three points in the plane, return whether these points are a boomerang.

**Example 1:**

```
Input: [[1,1],[2,3],[3,2]]
Output: true
```

**Example 2:**

```
Input: [[1,1],[2,2],[3,3]]
Output: false
```

这个题就是判断三个点是不是在一个直线上，或者这三个点是不是有重复的，判断的条件就是：

- 三个点是不是有相同的；
- 如果存在横坐标相差都是 0 的说明在一条直线是那个；
- 如果只有一个为零，另一个不为零，说明一定不在一个直线上；
- 如果斜率相等说明在一个直线上；

```java
class Solution {
    public boolean isBoomerang(int[][] points) {
        double a = points[0][0] - points[1][0];
        double c = points[0][1] - points[1][1];
        double b = points[0][0] - points[2][0];
        double d = points[0][1] - points[2][1];
        int j = 0;
        for(int i = 0;i < 3;i++) {
            j = i + 1;
            while(j < 3) {
                if(points[i][0] == points[j][0] && points[i][1] == points[j][1]) {
                    return false;
                }
                j++;
            }
        }  
        if(a == 0 && b == 0) return false;
        if(a == 0 || b == 0) return true;
        if(c / a == d / b) return false;
        return true;
        
    }
}
```

# Leetcode 1038