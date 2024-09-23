# python编程：从入门到实践

## 起步

1. 搭建编程环境
2. print("Hello World!")

## 变量和基本数据类型

### 变量的命名规范

### 基本数据类型

#### 数

1. int（）：python只有这一种整数类型
2. float
3. complex
4. bool：基于int，是数字0/1

使用下划线分隔数，更好阅读

#### 字符串

​	没有单独的字符类型，只有str

字符串的处理函数：

+ upper/lower
+ title
+ 去除前后空白

### 注释

## 列表

1. 如何访问：前序和后序
2. 增删改查：
   + append
   + pop/pop（index）
   + remove
   + a[index]=?/x
3. 列表方法：
   + sort（）/sort（reverse="True"）
   + sorted()
   + len()

注意处理索引问题

### 操作列表

1. 如何遍历：for i in a：# do something
2. 数值列表的操作
   + 创建
   + 操作函数：sum(),min(),max()
3. 列表解析：a=[function() for i in range(2,100)]
4. 使用列表的一部分
   1. 切片
   2. 拷贝列表：使用切片，a=[1,2,3],b=a[:] (not b=a)
5. 元组：不可修改的列表，用()来创建
   1. 提供保护
   2. 各种不可变类型的好处

## if语句

### 多种检查条件

1. 相等/不相等
2. 数值大小
3. 检查多个条件：and or
4. 检查元素的存在性：if a in b： if a not in b

### 多种检查语句

if

ifelse

if elif else

if elif elif

## 字典

###  使用字典

for k,v in dict.items():

for v in dict.valus():

for k in dict.keys():

增删改查：删除：del

通过get来防止访问不存在的key时直接报错退出，可以设置不存在时的默认返回值

字典可以是一个对象的多种不同属性，也可以是多个对象的相同属性

## 嵌套

## 用户输入和while

### input

prompt+返回str

可用int（）转换

### while

1. 单个条件变量控制
2. 多个变量共同使用flag控制
3. 使用break

### 使用while循环来增减列表中的各个元素

