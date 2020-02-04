[TOC]

# 1. Leetcode 705（HashSet构建）

构造一个HashSet：

其实构造一个HashSet有很多的方法，比如直接构造一个固定长度的Array也是可以的；

这个的构造思路比较灵活，并且涵盖了很多的不同的数据结构和算法设计：

- 首先整体的数据结构是一个 BSTNode[ ] 其中的每一个元素都是二叉排序树的树组，利用树的结构避免重复，并且在遍历的时候无论多长都是 logN 的时间复杂度，比较容易接受；
  - 对于元素的 add 就是在对应的数组位置上的BST的node上的添加；
  - 对于删除也是在对应的BST上的删除；
  - 在查看是否有对应元素的时候也是相同的操作，遍历整棵树；
- 其次是添加了rehash的操作，在添加的元素很多的时候，大于整个数组的长度一定百分比的时候，进行"扩容"，就是将原来的数组扩充为2倍；
  - 遍历原来的数组中的每一个 BST 对其中的元素进行BFS遍历放进Queue中从中取出来放进一个LinkedLIst中去，主要是为了获取List的迭代器  ListIterator it = linkedBST.listIterator( )；然后把这些元素重新加入到新扩充到数组中；

```java
class MyHashSet {
    BSTNode[] shelf;
    int eleNum;
    final static double rehashRate = 0.7;
    final static int initialSize = 1; 
    /** Initialize your data structure here. */
    public MyHashSet() {
        shelf = (BSTNode[]) new BSTNode[initialSize];
        eleNum = 1;
    }
    
    public int hash(int key) {
        return key % shelf.length;
    }
    public void rehash() {
        BSTNode[] newShelf = new BSTNode[shelf.length * 2];
        BSTNode[] old = shelf;
        shelf = newShelf;
        for(BSTNode node:old) {
            if(node != null) {
                LinkedList<BSTNode> linkedBST = node.LinkedBST();
                ListIterator it = linkedBST.listIterator();
                while(it.hasNext()) {
                    BSTNode linkedNode = (BSTNode)it.next();
                    add(linkedNode.data);
                }
            }
        }
    }
    public void add(int key) {
        BSTNode node = new BSTNode(key);
        int pos = hash(key);
        if(shelf[pos] == null) {
            shelf[pos] = node;
        }else {
            shelf[pos].add(node);
        }
        eleNum++;
        if(eleNum > rehashRate * shelf.length) {
            rehash();
        }
    }
    public void remove(int key) {
        int pos = hash(key);
        if(shelf[pos] != null) {
            shelf[pos] = shelf[pos].remove(key);
            eleNum--;
        }
    }  
    /** Returns true if this set contains the specified element */
    public boolean contains(int key) {
        int pos = hash(key);
        if(shelf[pos] != null) {
            return shelf[pos].contains(key);
        }
        return false;
    }  
    private class BSTNode {
        public int data;
        private BSTNode right;
        private BSTNode left;
        
        protected BSTNode(int data) {
            this.data = data;
        }        
        protected void add(BSTNode node) {
            if(node.data > this.data) {
                if(this.right == null) {
                    this.right = node;
                }else {
                    this.right.add(node);
                }
            }else if(node.data < this.data) {
                if(this.left == null) {
                    this.left = node;
                }else {
                    this.left.add(node);
                }
            }
        }     
        protected LinkedList<BSTNode> LinkedBST() {
            Queue<BSTNode> qu = new LinkedList<>();
            qu.add(this);
            LinkedList<BSTNode> li = new LinkedList<>();
            while(!qu.isEmpty()) {
                BSTNode curNode = qu.poll();
                li.add(curNode);
                if(curNode.left != null) qu.add(curNode.left);
                if(curNode.right != null) qu.add(curNode.right);
            }
            return li;
        }   
        protected boolean contains(int data) {
            if(this.data == data) {
                return true;
            }
            if(data < this.data && this.left != null) {
                return this.left.contains(data);
            }else if(data > this.data && this.right != null) {
                return this.right.contains(data);
            }
            return false;
        }       
        protected BSTNode remove(int data) {
            if(this.data == data) {
                if(this.left == null && this.right == null) {
                    return null;
                }
                if(this.left == null || this. right == null) {
                    return this.left == null?this.right:this.left;
                }
                this.data = this.left.findMax().data;
                this.left.remove(this.data);
            }else if(data < this.data && this.left != null) {
                this.left = this.left.remove(data);
            }else if(data > this.data && this.right != null) {
                this.right = this.right.remove(data);
            }
            return this;
        }
        
        protected BSTNode findMax() {
            BSTNode node = this;
            while(node.right != null) {
                node = node.right;
            }
            return node;
        }
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */
```

# 2. Leetcode 706（HashMap构建）

构建HashMap实现add，remove，get操作；

- 主要的数据结构是一个数组，数组中的元素是ListNode；
  - 重要的是每一个数组的第一个元素是一个假的头部节点（key：-1，value：-1）；
- 实现无论是哪一个操作都需要一个find( )函数找到合适的节点；
  - 首先hash定位到数组的位置pos；
  - 在这个 listNode 中找到给定 key 的 listNode，listNode是一个链表；直到当前为null，或者找到指定key的listNode才停止；返回的是最后的节点的上一个；如果返回的节点的下一个是null，说明没有找到带有指定 key 的 listNode；
  - 为了使得每一次的遍历至少返回一个节点，即使是被去掉的节点，所以每一个listNode都放上一个fake node；

```java
class MyHashMap {
    final ListNode[] nodes = new ListNode[10000];
    /** Initialize your data structure here. */
    public MyHashMap() {
        
    }
    public int hash(int key) {
        return Integer.hashCode(key) % nodes.length;
    }   
    /** value will always be non-negative. */
    public void put(int key, int value) {
        int pos = hash(key);
        if(nodes[pos] == null) {
            nodes[pos] = new ListNode(-1,-1);
        }
        ListNode findNode = find(nodes[pos],key);
        if(findNode.next != null) {
            findNode.next.value = value;
        }else {
            findNode.next = new ListNode(key,value);
        }
    }
    public ListNode find(ListNode ln,int key) {
        ListNode lastNode = null;
        ListNode node = ln;
        while(node != null && node.key != key) {
            lastNode = node;
            node = node.next;
        }
        return lastNode;
    }
    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    public int get(int key) {
        int pos = hash(key);
        if(nodes[pos] == null) return -1;
        ListNode findNode = find(nodes[pos],key);
        return findNode.next == null?-1:findNode.next.value;
    }
    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    public void remove(int key) {
        int i = hash(key);
        if (nodes[i] == null) return;
        ListNode prev = find(nodes[i], key);
        if (prev.next == null) return;
        prev.next = prev.next.next;
    }
    public class ListNode {
        public int key;
        public int value;
        public ListNode next;
        public ListNode(int key,int value) {
            this.key = key;
            this.value = value;
        }
    }
}
/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */
```

