# 基本数据类型

## number

### 数据类型

+ int
+ float
+ complex

### 数据操作

+ +，-，*，/，%
+ //：整除，返回整数部分

### 常用函数

+ abs(x)：绝对值
+ pow(x,y)：x的y次方
+ sqrt(x)：开方

## List

python 的list可以用不同的类型 a=[1，2，"abs"]

python的list在底层使用c的指针数组存储，同时每个节点保有前后向指针，可以实现双向遍历。指针数组中存储着指向当前元素的内存地址。所以可以存储不同的元素类型。

### 常用函数

1. **append()**增加： a.append(x),添加到数组末尾

   内部动态扩容/缩容，先开辟内存空间存储x，然后将x的内存地址放置在指针数组中。

2. **pop()**删除：

   a.pop(0)，删除下标为0的elemnt，a.pop()会删除最后一个element,返回删除元素的值.

   减少size，忽略该内存空间，下次写时覆盖。

3. **clear()** :清空，size置零
4. **del**:删除，减少内部每一个元素的引用计数器，减少链表的引用计数器，如果==0则将该链表放入python内部的链表缓存器，供下次申请链表空间时使用，减少开辟内存空间的开销。

python使用c的rellocate来分配内存，它的机制是先看当前内存空间后是否有足够的空内存，如果有直接开辟，如果没有寻找新的整块内存再进行复制，该机制减少了一部分复制开销。

1. **len(a):**返回数组长度

2. **max(a)**:a的最大值

3. **min(a)**:a的最小值

4. 遍历方法

   ```py
   for x in a:
       print(x)# 循环次数等于数组的长度
   for index in range(0,10):
       print(a[index])
   ```

 5. 查找

    ```python
    3 in a #返回true or false
    ```

6. slice

   ```python
   a[1:3]# 返回[a[1],a[2],a[2]]
   #返回原数组中的值[a,b)
   a[:]#返回全部
   a[0:-1]#a[n],返回前n-1个
   ```

### 高级表达

```python
a=[1,2,3,4]
b=[i*i for i in a]
#b=[1,4,9,16]
c=len(a)*[0]
#c=[0,0,0,0]
```



## Tuple

同样的，tuple也是一个可以存储多种类型的，和list不同的区别在于其不可迭代，不可以修改/增加/删除。

### 常用函数：

同list，通常在我们只需要查找时使用Tuple。其余操作和list相同。

### list和tuple间的转换

```python
b=list(a)
```

## Set

特点：所有元素唯一

### 常用函数

1. **add()**:会保证唯一性
2. **update(set)**:将两个set合并
3. **remove(x)**:移除val==x的数

### 集合交并补操作

1. a - b：求差集，返回差集
2. a | b：求并集
3. a & b：求交集
4. a ^ b：全集-交集

## Dictionary

 键值对组

### 常用函数

1. 查：dict["name"]

2. 增/改：dict["name"]="ShaoJingwen"

3. 删除： dict.pop("key")

4. 遍历方法：

   ```python
   k in dict# return true or false
   for key in dict:
       print(key)
   for value in dict.value:
       print(value)
   for k,v in dict:
       print("key"+k+"value"+v)
   ```

## String

由字符组成的数组

### 常用函数

1. **len()**：返回字符串长度

2. **max(s),min(s)**：返回s中最大的字母/最小的字母

3. **count("x")**:返回x的个数

4. **isupper()/islower()**:判断s中字母是否都是大写/小写

5. **isdigit()**:是否全是数字

6. **lower()/upper()**:全部大写/全部小写

7. **strip()/lstrip()/rstrip()**:去除前后空格/去除左边空格/去除右边空格

8. **swapcase()**:交换大小写

9. **replace("x","y")**:把字符串中的x全部换成y

10. **spilt("x")**:以x为分割符分割原本的字符串并返回字符串数组

11. **join()**: separator.join(iterable)

    + `separator`：用于分隔的字符串。
    + `iterable`：可迭代对象，其元素必须是字符串类型。

12. **sorted**：

    ```python
    sorted(iterable, key=None, reverse=False)
    ```

    - `iterable`：要排序的可迭代对象。
    - `key`（可选）：一个函数，如果提供了此参数，将对每个元素调用一次该函数，并按照函数返回值排序。
    - `reverse`（可选）：一个布尔值，如果设为 `True`，将按降序排序，默认值为 `False`。

#  常用数据结构

## Array

增删查改效率问题

表示方法：list

 ## LinkList

增删查改效率

表示方法：定义节点数据结构

## HashTable

表示方法：dict实现

每一个key通过hash算法对应一个内存地址，能够实现很快的search

## Queue

1. 先进先出

2. 双端队列，两边可以出

表示方法：

1. list：pop删除比较慢，更常用下面的

2. **from collections import deque**：

   ```python
   from collections import deque
   
   d=deque([1,2,23,2,1])
   append()
   pop()
   appendleft()
   popleft()
   ```

## Stack

先入后出

表示方法：

1. deque
2. **list**

## Heap

分为最大堆和最小堆

表示方法：

1. from heapq import heapify, heappush, heappop

   ```python
   heap= heapify([1,2,3,4]) # 默认小堆，大堆加-
   heappush(heap,5)
   heappop(heap)->1
   nlargest(2,heap) # 找前n个最大值
   nsmallest(2,heap) # 找前n个最小值
    
   ```

## Tree



