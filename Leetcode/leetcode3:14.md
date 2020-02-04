[TOC]



# 1.Leetcode 983（DP）

In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will travel is given as an array `days`.  Each day is an integer from `1` to `365`.

Train tickets are sold in 3 different ways:

- a 1-day pass is sold for `costs[0]` dollars;
- a 7-day pass is sold for `costs[1]` dollars;
- a 30-day pass is sold for `costs[2]` dollars.

The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of `days`.

## 思路1

第一种思路是用两个队列分别存储当前这一天如果出游的话，那么前一次出游的最小的花费cost和此次购买7天票或者30天票的花费，队列中的第一个元素是距离当前出行日期30天或者7天内最远的那个日期。整体的思路就是不断的跟随日期往后推移，不断的判断是在过去的某一天购买7/30的票合算还是在上一次的出游最小花费cost的基础上此次的出行单独的花费一次。总的来说，如果此次的出行的时间距离上次的出行时间很远那么此次的出行就是应该单独购票，应为之前的出行购买的7/30不能够cover此次的出行。DP的思想体现在在小范围的最优解在新出现的事情上进行合理的规划得到最新情况的最优解。

```java
public class MinCostForTicketsOne {
    public int minCost(int[] days,int[] costs) {
        Queue<int[]> seven = new LinkedList<>();
        Queue<int[]> thirty = new LinkedList<>();
        int cost = 0;
        for(int day:days) {
            while(!seven.isEmpty() && seven.peek()[0] + 7 <= day) {
                seven.poll();
            }
            while(!thirty.isEmpty() && thirty.peek()[0] + 30 <= day) {
                thirty.poll();
            }
            int [] s = new int[2];
            int [] t = new int[2];
            s[0] = day;
            t[0] = day;
            s[1] = cost + costs[1];
            t[1] = cost + costs[2];
            seven.offer(s);
            thirty.offer(t);
            cost = Math.min(cost+costs[0],seven.peek()[1]);
            cost = Math.min(cost,thirty.peek()[1]);
        }
        return cost;
    }
}
```

## 思路2

因为整个行程都是在365天的行程，所以和思路一不同的地方在于这次是“回头”观察，在每一天都会更新在这一天之前的所有的行程的最小的花费，如果这个日期不是在行程当中的，那么就会按照行程的花费：

```java
dp[i] = dp[i - 1]
```

如果是在行程中出现的，那么要做的就是回顾，在距这次行程7/30天的时候如果购买的是7/30的票那么和在这次行程购买本次的单独票的价格的比较。

```java
class Solution {
    public int mincostTickets(int[] days, int[] costs) {
        boolean[] travelSchedual = new boolean[366];
        for(int day:days) {
            travelSchedual[day] = true;
        }
        int cost = 0;
        int size = days.length;
        int[] dp = new int[366];
        for(int i = 1;i < 366;i++) {
            if(!travelSchedual[i]) {
                dp[i] = dp[i - 1];
            }else {
                dp[i] = Math.min(dp[Math.max(0,i - 7)] + costs[1],dp[i - 1] + costs[0]);
                dp[i] = Math.min(dp[Math.max(0,i - 30)] + costs[2],dp[i]);
            }
        }
        return dp[365];
    }
}
```

# 2.Leetcode 322（DP）

You are given coins of different denominations and a total amount of money *amount*. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

这道题的意思就是给你三个面值的硬币判断是否可以组成目标价格，并且用尽可能少的硬币；不能组成的话就返回-1；

思路的话就是将目标设置成为数组的长度，不断用coin的面值去填充，例如先用面值为1的硬币去填充，所谓填充就是找到在目标数值以内用不同的硬币的最小的数量。

```java
class Solution {
    public int coinChange(int[] coins, int amount) {
        if(amount < 1) {
            return 0;
        }
        int[] a = new int[amount+1];
        Arrays.fill(a,Integer.MAX_VALUE);
        a[0] = 0;
        for(int coin:coins) {
            for(int i = coin;i <= amount;i++) {
                if(a[i - coin] != Integer.MAX_VALUE) {
                    a[i] = Math.min(a[i - coin] + 1,a[i]);
                }
            }
        }
        return a[amount] == Integer.MAX_VALUE ? -1:a[amount];     
    }
}
```

# 3.Leetcode 309（DP）

Say you have an array for which the *i*th element is the price of a given stock on day *i*.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

- You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
- After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

和之前的无限制买卖股票类似主要是加入了在一次交易之后进行休息一次的coolDown机制。所以就是说在之前的不限制购买时间的基础上限制每一次购买的时候根据的不能是上一次的卖出价格而必须是上上次的卖出价格。就是说每一次的合适的购买都应该前天的最佳卖出拥有的获利。

```java
class Solution {
    public int maxProfit(int[] prices) {
        int size = prices.length;
        if(size < 2) {
            return 0;
        }
        int b0 = -prices[0];
        int b1 = b0;
        int s0 = 0;int s1 = 0;int s2 = 0;
        for(int i = 1;i < size;i++) {
            b0 = Math.max(b1,s2 - prices[i]);
            s0 = Math.max(s1,b1+prices[i]);
            s2  = s1;s1 = s0;
            b1 = b0;
        }
        return s0;
    }
}
```





