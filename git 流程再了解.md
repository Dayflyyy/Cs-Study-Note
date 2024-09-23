# git 流程再了解

今天重新了解了git的commit checkout branch 命令

## 分支概念

分支其实是一个指向具体提交号的指针，创建分支就是创建了一个指针，开销很小，可以建很多个分支

## HEAD 概念

HEAD是当前工作的指针,提交时实际上是从head当前指向的节点进行提交

![image-20240911100959956](C:\Users\dayfly\AppData\Roaming\Typora\typora-user-images\image-20240911100959956.png)

使用git checkout 实际上是改变head指针的位置，checkout既可以通过指定分支名切换到分支（分支和head同时移动），也可以通过指向提交名指向具体的提交（分离head状态），