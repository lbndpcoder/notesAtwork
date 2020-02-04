[TOC]

本周的 leetcode 主要是

- 构建二叉树的方法；
- 公共父节点的递归/非递归

# <1> Construct Binary Tree from ?

构建二叉树主要是通过前序/后序/中序数组进行构建；

其中利用（中序/后序）或者（中序/前序）的思路是很相同的主要是：

- 遍历后序/前序的元素，找到在中序数组中的位置；
- 所处位置的左边的元素就是左子树；
- 右侧为右子树；
- 时间复杂度为 O(N)；

## <1.1> 106 中序后序构建二叉树

```java
class Solution {
    public TreeNode buildTree(int[] in, int[] post) {
        HashMap<Integer,Integer> map = new HashMap<>();
        int count = 0;
        for(int num:in) {
            map.put(num,count++);
        }
        return helper(map,in,post,0,in.length - 1,0);
    }
    public TreeNode helper(HashMap<Integer,Integer> map,int[] in,int[] post,int start,int end,int offset) {
        if(start > end) {
            return null;
        }
        TreeNode node = new TreeNode(post[end - offset]);
        int index = map.get(post[end - offset]);
        node.left = helper(map,in,post,start,index - 1,offset);
        node.right = helper(map,in,post,index + 1,end,offset + 1);
        return node;
    }
}
```

## <1.2> 105 前序中序构建二叉树

相对于后序中序构建二叉树来说，前序构建的思路是一样的,只不过从数组的前面开始遍历时间复杂度也都是相同.

```java
class Solution {
    public TreeNode buildTree(int[] pre, int[] in) {
        HashMap<Integer,Integer> map = new HashMap<>();
        for(int i = 0;i < in.length;i++) {
            map.put(in[i],i);
        }
        return helper(map,0,in.length-1,0,pre,in);
    }
    public TreeNode helper(HashMap<Integer,Integer> map,int start,int end,int offset,int[] pre,int[] in) {
        if(start > end) return null;
        int index = map.get(pre[start + offset]);
        TreeNode node = new TreeNode(pre[start + offset]);
        node.left = helper(map,start,index-1,offset + 1,pre,in);
        node.right = helper(map,index + 1,end,offset,pre,in);
        return node;
    }
}
```

## <1.3> 889 前序后序构建二叉树

和前面的递归的思路不同，遍历先序数组，将其中的元素放入栈中，当栈顶的元素和后序数组相同的时候，说明此时一侧（左子树/右子树）已经构造完了；

```java
class Solution {
    public TreeNode constructFromPrePost(int[] pre, int[] post) {
        Stack<TreeNode> st = new Stack<>();
        TreeNode node = new TreeNode(pre[0]);
        st.push(node);
        for(int i = 1,j = 0;i < pre.length;i++) {
            TreeNode temp = new TreeNode(pre[i]);
            while(st.peek().val == post[j]) {
                st.pop();
                j++;
            }
            if(st.peek().left == null) {
                st.peek().left = temp;
            }else {
                st.peek().right = temp;
            }
            st.push(temp);
        }
        return node;
    }
}
```

## <1.4> 1008 前序构造BST

思路和利用前序/后序构造的思路是一样，利用栈，如果当前的遍历的元素大于栈顶的元素，那么弹出栈，找到此时对应的根节点，如果栈顶的元素大于此时的元素的数值，那么说明刚被弹出栈的元素应该是此时元素的根节点。

```java
class Solution {
    public TreeNode bstFromPreorder(int[] pre) {
        Stack<TreeNode> st = new Stack<>();
        TreeNode root = new TreeNode(pre[0]);
        st.push(root);
        TreeNode temp = root;
        for(int i = 1;i < pre.length;i++) {
            TreeNode node = new TreeNode(pre[i]);
            while(!st.isEmpty() && pre[i] > st.peek().val) {
                temp = st.pop();
            }
            if(node.val > temp.val) {
                temp.right = node;
                temp = temp.right;
            }else {
                temp.left = node;
                temp = temp.left;
            }
            st.push(node);
        }
        return root;
    }
}
```

# <2> 公共父节点

## <2.1> 递归方法

 首先就是判断左右节点是否存在目标节点p，q；

- 当前的左右都存在目标，那么返回当前的节点；
- 如果当前只存在一侧返回这一侧；

```java
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root == null) return null;
        if(root == p || root == q) return root;
        TreeNode left = lowestCommonAncestor(root.left,p,q);
        TreeNode right = lowestCommonAncestor(root.right,p,q);
        if(left != null && right != null) {
            return root;
        }else if(left != null) {
            return left;
        }else if(right != null) {
            return right;
        }
        return null;
    }
}
```

## <2.2> 非递归方法

利用 栈 和 hashmap：

- 栈 的作用是进行层次遍历；
- map 的作用是把所有的子节点和其父亲节点对应上；

将所有的子节点和其父亲节点对应上之后，将从 p 节点到根节点的所有的路径上的节点存储起来，然后和 q 节点到根节点的路径上的所有节点有交叉的就是要求的节点：

```java

```

