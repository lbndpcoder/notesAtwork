[TOC]

# 1. Leetcode 49（Hash）

Given an array of strings, group anagrams together.

**Example:**

```
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```

将"异位”的放在一起，异位的意思就是两个单词含有相同的字母但是放的顺序不同：

- 将 String 数组中每一个 String 变成 char[ ] 然后排序，这样如果是异位的单词都会相同，然后放在 HashMap中；
- 判断如果存在排序后的单词，那么就放在 map<String,List<String>>  中；

```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if(strs == null) return new ArrayList<List<String>>(); 
        HashMap<String,List<String>> m = new HashMap<>();
        for(String str:strs) {
            char[] c = str.toCharArray();
            Arrays.sort(c);
            String keyStr = String.valueOf(c);
            if(!m.containsKey(keyStr)) {
                List<String> l = new ArrayList<>();
                l.add(str);
                m.put(keyStr,l);
            }else {
                m.get(keyStr).add(str);
            }
        }
        return new ArrayList<List<String>>(m.values());
    }
}
```

# 2. Leetcode 36（Hash）

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated **according to the following rules**:

1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the 9 `3x3` sub-boxes of the grid must contain the digits `1-9` without repetition.

![img](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)

这是一个数独的问题，满足下面三个条件才能返回 True：

- 每一行都必须是 1-9 的数字，不能有重复；
- 每一列也必须是 1-9 的数字，不能有重复；
- 每一个小的 3*3 的方格也必须是 1-9 的数字不能重复；

所以就是要判断在遍历每一个点的时候每一个条件是不是符合：

- 在每一行的遍历的时候利用一个数组就可以解决，将遍历到的数值作为index放进nums[index ] = 1；如果在这一行遍历的过程中发生重复的数值就返回false；
- 在每一列的遍历需要一个 HashMap 将每一列对应一个数组，遍历到这列的时候如果存在重复返回false；
- 在每一个小的 3*3 的方格中需要重新定义坐标：
  - 定义一个loc\[3][3]的数组并将遍历的到的数值的坐标转换为对应的小方格的坐标，小方格的标号为1-9；
  - 遍历到的坐标—>小方格的坐标—>小方格的编号—>对应的 HashMap 中的数组；

```java
class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashMap<Integer,int[]> map = new HashMap<>();
        int[][] loc = new int[3][3];
        int count = 0;
        for(int i = 0;i < 3;i++) {
            for(int j = 0;j < 3;j++) {
                loc[i][j] = count++;
            }
        }
        HashMap<Integer,int[]> map2 = new HashMap<>();
        for(int i = 0;i < 9;i++) {
            int[] nums = new int[9];
            for(int j = 0;j < 9;j++) {
                if(board[i][j] == '.') {
                    continue;
                }
                int pos = board[i][j] - '0' - 1;
                int bigI = i / 3;
                int bigJ = j / 3;
                if(!map2.containsKey(loc[bigI][bigJ])) {
                    int[] temp = new int[9];
                    temp[pos] = 1;
                    map2.put(loc[bigI][bigJ],temp);
                }else {
                    if(map2.get(loc[bigI][bigJ])[pos] == 1) {
                       return false;
                    }else {
                        int[] a = map2.get(loc[bigI][bigJ]);
                        a[pos] = 1;
                        map2.put(loc[bigI][bigJ],a);
                    }
                }
                if(!map.containsKey(j)) {
                    int[] tempNums = new int[9];
                    tempNums[pos] = 1;
                    map.put(j,tempNums);
                }else {
                    if(map.get(j)[pos] == 1) {
                        return false;
                    }else {
                        int[] temp = map.get(j);
                        temp[pos] = 1;
                        map.put(j,temp);
                    }
                }
                if(nums[pos] == 1) return false;
                nums[pos] = 1;
            }
        }
        return true;
    }
}
```

