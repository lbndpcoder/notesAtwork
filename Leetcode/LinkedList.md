[TOC]

# LinkedList

##（1）206. Reverse Linked List

反转链表：

- 第一个位置的 head 节点的下一个链接到 node 节点；
- node 变为 head；
- head 变为其链接前的下一个节点 temp ；

## （2）328. Odd Even Linked List

将偶数位置的节点链在奇数位置的节点上面；

- 设置两个指针even / odd，当下一个节点不是空的时候，一直跳到下一个的下一个；
- 分别将 even 和 odd 位置的节点链在一起；

##（3）92. Reverse Linked List II

将给定范围内的链表进行反转：如图所示：

![lk](/Users/liubonan/Documents/Leetcode/lkk.png)

如图所示：

- 首先找到初始的位置 m 的前一个位置设置为 pre 节点；
- m 位置为 start 节点；start 的下一个节点为 then ；
- 将 start 的下一个节点指向的 then 的下一个节点；
- then 节点指向它的前一个节点（也就是 pre 的下一个节点）；
- pre 的下一个指向 then 节点；
- then 变成它的下一个节点；

## （4）2. Add Two Numbers

两个链表求和，主要在于使用的是头插法和进位的判断；

- 首先依次将两个链表的元素相加，计算每一位的数值和进位；
- 直到一个链表的结束；
- 判断另外一个链表；
- 判断是不是还有进位；

## （5）86. Partition List

​	将一个链表分成两个部分，其中的前面的部分小于一个数值，后面部分大于一个数值，并且这些数值的顺序不能变。

- 分别构建两个链表一个链表，遍历整个原链表；
  - 如果小于目标数值那就链在其中的一个；
  - 大于目标就链到另一个；

##（6）83. Remove Duplicates from Sorted List

​	删除一个有序链表中的重复的元素，两个指针pre ， head 分别遍历，如果相同的数值，那么其中的一个指针向后移动，直到两个指针所指的元素不同的时候，将 pre 所指的节点链到 head 上面；head 继续移动到下一个节点；

##（7）82. Remove Duplicates from Sorted List 2

​	删除其中的所有的重复元素，和 83 不同在于此时要删除所有的重复的元素。首先还是设置两个指针，pre ， 正常的 head 。

- 设置一个 fake 节点作为 pre 的初始节点，下一个节点为 head 节点；
- 如果 pre 的下一个节点不等于 head 的下一个节点：
  - 如果 pre 的下一个就是 head 说明 pre 可以跳到 head 的位置，因为有序并且不重复；
  - 如果 pre 的下一个不是 head 有可能是[2,2,3,3]这种情况， 所以讲 pre 的下一个链接到 head.next ； 
- 如果最后 pre 最后的下一个不是 head ，说明 head 一直在 next ，pre 的下一个一直和 head 的下一个相同，所以知道链表的末尾，pre 的下一个为null；

​    总的来说一共有两种情况，一种是 pre 的下一个位于一连串的相同的节点的初始上，一种是跟随 head 在不同的节点上；

##（8）725. Split Linked List in Parts

​	将一个链表分成规定的部分，按照顺序划分成多个链表，并且要求前面的每一份中含有的节点个数要多；

- 首先计算出每一份应该有的节点的个数：
  - 如果整个 list 的长度是3，但是要分成 5 份 那么说明每一个应该有的就是 0 个节点；
- 但是我们的目标不是每一份中是 0 个节点，所以还需要求出来余数作为剩余的节点个数 N ，这些节点就去补充前面的 N 份，每一份在原有的个数上面 +1 。
- 在每一份中，注意末尾的节点要将它的下一个节点变为 null ；

##（9）19. Remove Nth Node From End of List

​	删除从后面数的第 N 个节点，使用快慢指针的思路：

- 设置一个 fake 头节点，为了在整个链表只有一个节点的时候解决问题；
- 将 slow ，fast 都在 fake 上；
  - 首先 fast 向后移动 N 个位置，找到距离 slow 距离为 N 的位置；
  - slow，fast 一起移动，直到链表的末尾；
- 将 slow 的节点的下一个指向，slow的下一个的下一个，删除目标节点；

## （10）24. Swap Nodes in Pairs

​	将链表中的每两个节点为一组，调换位置：和第（3）个题的思路比较相似：

- 设置一个 fake 的头节点：用 pre 初始指向头节点；
  - 将 pre 的下一个指向 head 的下一个；
  - pre 变成当前的 head ；
  - head 的下一个节点的下一个指向 head ；
  - head 的下一个指向 head 的下一个的下一个；

##（11）25. Reverse Nodes in k-Group

 设定一个 k 的数值，将一个链表从前向后的每 k 个节点反转；

- 如果当前节点向后遍历第 k 个节点为 null ，那么就返回最开始的节点；
- 如果不为空，进入下一个递归；
- 用当前的头节点与上一个的递归的返回数值相连；

## （12）138. Copy List with Random Pointer

## （13）141. Linked List Cycle

判断链表是不是有环，将链表进行反转，顺着反转的链表，如果有环就可以返回原来的头节点；

## （14）142. Linked List Cycle II

这个题和上面的题基本上是一个题，这里再说一下：

- 有重复的元素；
- 不能改变原来的链表；
- 利用快慢指针；

![linked](/Users/liubonan/Documents/Leetcode/linked.png)

​	在利用快慢指针的时候，第一次两个指针相遇的位置为 N-k-M ，假设第一次相遇 fast 指针走了 x2 轮的 N-k ，slow指针走了 x1 轮的 N-k 指针：
$$
\begin{aligned}
2[x_1(N-k)+(N-M)] &= x_2(N-k)+(N-M)\\
2x_1(N-k)+(N-M)&= x_2(N-k)
\end{aligned}
$$
可以得到fast 指针走的较快所以走的路程是slow指针走的路程的 2 倍 。所以可以得到上面的等式； 
$$
N-M = (x_2-2x_1)(N-K)
$$
所以可以假设 w，并得到：
$$
x_2 - 2x_1 = w \\
N-M = w(N-K) \\
wN-wK = N-M \\
wK-M=(w-1)N \\
K-M = (w-1)(N-K) \\
K=(w-1)(N-K)+M
$$
最终得到的公式可以说明，当在第一次相遇之后，将 slow / fast 从 head 节点两个再次出发，速度一样，最终的相遇的位置就是链表成环的位置；