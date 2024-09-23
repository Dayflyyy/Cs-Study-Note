# Python

## pythn语言特点

1. 解释性语言：没有编译过程
2. 交互语言：有交互界面
3. 面向对象
4. 可扩展/可嵌入：c/c++中可以内嵌python脚本，python中可以调用c/c++的函数（实现功能/性能需求）
5. 开源：已被移植到多个平台和系统上，有良好的可扩展性。
6. 库丰富：python标准库强大，第三方库丰富

云计算框架 overstack

## python 环境配置

由于python的开源特性，其在很多平台都可以运行，如果在你想使用的平台没办法使用二进制文件，也可以使用c编译器手动编译。

```bash
tar -zxvf Python-3.6.1.tgz
cd Python-3.6.1
./configure
make && make install
```

为了方便操作系统可以搜索到python的可执行文件，需要将python添加到环境变量

+ Unix

```bash
export PATH="$PATH:/the/place/your/python"
```

+ win:计算机-》属性-》高级系统设置-》配置path

## python基本语法

1. 标识符：`_`和字母开头，不能和关键词重复

2. keyword关键词：

   ```python
   keyword.kwlist
   ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
   ```

3. 注释：`#` +`"""`

4. 多行语句

   + 反斜杠

   ```python
   total = item_one + \
           item_two + \
           item_three
   ```

   + `[]`+`{}`+`()`中逗号分隔的可以在多行中

   ```python
   total = ['item_one', 
            'item_two', 
            'item_three',
           'item_four', 'item_five']
   ```

5. 基本数据类型

   + 数字：int+ float+ boolean+complex

   + 字符串：string

     + python没有字符数据类型

     + 可以使用`"""`创建多行字符串
     + 支持正反向索引，正向从零开始，反向从-1开始（-1，-2...）（底层双向链表存储）
     + 字符串切片：s[start:end :step​] （起始：终止：步长）

6. print输出

   ```python
   print(s,end="")#默认转行。通过end来改变分割符
   ```


## 基本功能函数



python中的number存储数据数字数据类型，数据类型是不允许改变的，这就意味着如果改变数字数据类型的值，将重新分配内存空间。



在不同的机器上浮点运算的值可能不一样？why



在交互模式中，最后被输出的表达式结果被赋值给变量 **_** 。例如：