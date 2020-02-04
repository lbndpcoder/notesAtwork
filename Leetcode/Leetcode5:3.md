[TOC]

# Sliding Window

## 1. Leetcode 239

### RAW (beat 100%)

### Deque (beat 60%)

#Leetcode 146

Design and implement a data structure for [Least Recently Used (LRU) cache](https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU). It should support the following operations: `get` and `put`.

`get(key)` - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
`put(key, value)` - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

**Follow up:**
Could you do both operations in **O(1)** time complexity?

**Example:**

```
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
```

设计一个 LRU ，主要面临的问题就是当内存区域满了的情况下，优先替换掉好久没有访问的数据；

- 利用一个 Hashtable 来存储每一个 key 和 "DoubleLinkedNode" ，这样可以使得在每一次的访问可以直接访问到要找到的数值；
- 整个 cache 是一个链表，由一个"虚假"的 Head ，和一个"虚假”的 Tail 组成，为了方便添加新的节点和删除尾部最后一个有数值的节点；
- DoubleLinkedNode 主要完成的操作是为了在每一次的 put 操作中：
  - 如果不存在这个节点，那么新建一个 Node ，并且判断这个链表中是不是存满了，如果存满了那么去掉尾部的节点；如果没有存满，那么加入到链表中并且放在最前面；
- 在每一次的 get 的操作，不仅得到要找到的要找到的 key 对应的节点并且要将找到的节点放在链表的最前面，这样在每一次满的时候删除尾部节点就不会删除掉最近访问的节点；

```java
import java.util.Hashtable;
class LRUCache {
    private class DoubleLinkedNode {
        DoubleLinkedNode next;
        DoubleLinkedNode pre;
        int key;
        int value;
    }

    private void addNode(DoubleLinkedNode node) {
        node.next = head.next;
        node.pre = head;
        head.next.pre = node;
        head.next = node;
    }
    private void removeNode(DoubleLinkedNode node) {
        node.pre.next = node.next;
        node.next.pre = node.pre;
    }
    private void removeToHead(DoubleLinkedNode node) {
        removeNode(node);
        addNode(node);
    }
    private DoubleLinkedNode popTail() {
        DoubleLinkedNode tailNode = tail.pre;
        removeNode(tailNode);
        return tailNode;
    }
    private Hashtable<Integer,DoubleLinkedNode> cache 
        = new Hashtable<>();
    private DoubleLinkedNode head;
    private DoubleLinkedNode tail;
    private int capacity;
    private int count;
    public LRUCache(int capacity) {
        this.capacity = capacity;
        count = 0;
        head = new DoubleLinkedNode();
        tail = new DoubleLinkedNode();
        head.next = tail;
        tail.next = null;
        head.pre = null;
        tail.pre = head;
    }
    
    public int get(int key) {
        DoubleLinkedNode node = cache.get(key);
        if(node == null) {
            return -1;
        }
        removeToHead(node);
        return node.value;
    }
    public void put(int key, int value) {
        DoubleLinkedNode node = cache.get(key);
        if(node == null) {
            DoubleLinkedNode newNode = new DoubleLinkedNode();
            newNode.key = key;
            newNode.value = value;
            cache.put(key,newNode);
            addNode(newNode);
            count++;
            if(count > capacity) {
                DoubleLinkedNode tailNode = popTail();
                cache.remove(tailNode.key);
                removeNode(tailNode);
                count--;
            }
        }else {
            node.value = value;
            removeToHead(node);
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
```

