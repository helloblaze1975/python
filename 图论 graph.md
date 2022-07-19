# [图论算法 graph](https://github.com/wangshusen/AdvancedAlgorithms)
[leecode 997法官](https://leetcode.cn/problems/find-the-town-judge/) 

[997视频](https://www.bilibili.com/video/BV1te411p7Q9/?spm_id_from=autoNext&vd_source=a470c1bdb350a1932aad2fb7ae722354)
[leecode 200 岛屿](https://www.bilibili.com/video/BV1Tr4y1K7bA?spm_id_from=333.337.search-card.all.click&vd_source=a470c1bdb350a1932aad2fb7ae722354)
>1. 如果存在法官，那么所有人都会信任法官，在结合条件1，可以得出信任法官的人数为n-1。
2. 如果不存在法官，那么也可能存在某些人被所有人信任，这个人的信任人数也为n-1，但是他也会信任别人。
3. 可以以此作为区分other和juage的条件，假设每个人都有信任值，那么定义一个数组长度为n，用来存放n个人的信任值:
   1. 如果一个人信任了别人，那么将这个人的信任值-1
   2. 如果一个人被别人信任，那么这个人的信任值＋1
   ![图](../../算法/images/996%20小镇法官.png)

当一个人被所有人信任，并且他没有信任其它人时，这个人的信任值就是n- 1，那么此人就是法官。
当一个人被所有人信任，但是他也信任了其他人时，这个人的信任值<n - 1。
其它情况下，每个人的信任值都会小于n -1

作者：liuduo-yu
链接：https://leetcode.cn/problems/find-the-town-judge/solution/ji-lu-yi-xia-mei-xue-guo-tu-kan-bie-ren-i7zub/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
## 基本概念
## 最短路
## 最小生成树
## 旅行售货员
### 问题引入与分析
1. 水灾最佳巡视路线
2. 图的常见类：
   1. image.png
3. 对应视频：
   # [游戏方式讲图论入门：](https://www.bilibili.com/video/BV1rD4y1S7j9?vd_source=a470c1bdb350a1932aad2fb7ae722354)

    ### 树的特点： 
    >树不能有回路： 任何节点间有且仅有一条路径的联通图
    >节点间必须是联通的 n-1条边
    >无向
    ### 树的计算公式：
    >n个节点 n-1条边
    ### 图和树的不同
    ### 图转成树 original graph  spanning tree
    > 最小生成树：（Minimum Spanning Tree）权重相加最小
   
     ### 1. [Prim's算法](https://www.bilibili.com/video/BV1A5411M7zc/?spm_id_from=333.788.recommend_more_video.0&vd_source=a470c1bdb350a1932aad2fb7ae722354)：O（n） 
   >从图中任意一点开始，选择权重最小的相邻边
       >
    >如果会形成循环的话，则选择权重次小的边，一次类推 
   
       
   ### 2. Kruskal's算法：
      1. . 过程： 
    > 创建队列把所有的边的权重从小到大排列 build a queue of edges, sort the elemnents so thant the weights are in ascending升序 order.
    >
    > 从升序方式遍历，给树加枝干 perform dequeue and get the edge ;if the nodes are not in the same tree两点之间没有红色路径,accept edge边
    >取除权重最小的那条边， 只要不形成循环就加入到最后的生成树中
    >
    >Initially, there are N trees;every vertex is a tree
    > Each iteration studies one edge; the edge may be chosen so that two trees are merged.
    > Stop when there is only one tree
    > the algorithm runs in at most 边 iterations. 
    2. 算法实现
      1. How to decide whether tow vertices are in the same tree? 接点是否在同一棵树中，是否存在红色路径
        > 1. using disjoint sets data structure 并查集存树节点
        > 2. put vertices of a tree in the same set. 时间复杂度低(常数)
       2. How to merge two tree?
        >union the two trees
    3. 时间复杂度 ： 
    > Time complexity o(m.logm)排序边的时间 


    [图的简单快速入门](https://www.cnblogs.com/labuladong/p/15830901.html)

    [ topological sort 怎么用向量表达有方向的图](https://www.hackerearth.com/practice/algorithms/graphs/topological-sort/tutorial/)