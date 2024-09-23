# Python Concurrent

python并发的支持主要由三部分组成

+ 多线程 threading
+ 多进程 multiprocessing
+ 协程 asyncio

python的这几个库同时也支持 锁、信号量 等机制来保护共享资源访问的一致性。

## python语言特点

### GIL

 ![image-20240822111520661](C:\Users\dayfly\AppData\Roaming\Typora\typora-user-images\image-20240822111520661.png)

因为python中对对象的管理使用共享计数器进行的，使用gil可以避免对计数器加锁，简化对共享资源的管理。

![image-20240822111801070](C:\Users\dayfly\AppData\Roaming\Typora\typora-user-images\image-20240822111801070.png)

在io过程中线程会暂时释放gil，此时两个线程可以同时进行io和cpu计算。但在cpu密集型任务时对于线程切换的花销更大，得不偿失。



## Threading 多线程

由于Python GIL(global interpreter lock)的存在，python在运行时最多只允许同一时间一个线程运行，但在io时该锁可以暂时放开，所以多线程适用于任务量少，并发量低，io密集型的任务

例如文件读写

```python
import threading #导入相关库

# 写明相关函数
def work(i):
    print(f"Threading {i} is working")

# 创建线程
t= Thread(target=work,args=(1))

# 启动线程
t.start()

# 等待线程结束
t.join()
```

## multiprocessing 多进程

![image-20240822121756137](C:\Users\dayfly\AppData\Roaming\Typora\typora-user-images\image-20240822121756137.png)

通过导入多进程库，可以实现对多核CPU更好的利用，每个进程有自己单独的解释器和内存空间。多进程更适合cpu密集型任务，例如计算/解压缩/解加密

```python
import multiprocessing # 导入相关库

# 写明相关函数
def work(i):
    print(f"Process {i} is working now...")

# 创建进程
p= Processs(target=work,args=(1,))

# 开启进程
p.start()

# 等待进程
p.join()

```

## 池化——Thread & multiprocessing

通过future库来实现池化操作。

### 线程池原理

通过重用线程来减少新建和终止线程的开销，适用于短期内突发的大量短耗时相同请求。

![image-20240822115959942](C:\Users\dayfly\AppData\Roaming\Typora\typora-user-images\image-20240822115959942.png)

**线程池优势：**

1. 减少新建/终止成本
2. 防御功能：防止创建过多线程导致系统负荷过高

一般来说线程池的默认线程数是 **cpu核心数+4**

### 线程池化

``` python
import concurrent.futures
import threading
 
# 定义线程要执行的函数
def worker(index):
    print(f"Thread {index} is starting")
    print(f"Thread {index} is done")
 
# 使用线程池创建多线程
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # 方式1
    futures = [executor.submit(worker, i) for i in range(5)]
    # 方式2
    #####  map的结果顺序和参数列表的入参顺序是一样的 ####
   	results = executor.map(worker,[1,2,3])
# 等待所有线程完成
concurrent.futures.wait(futures)
 
print("All threads are done")
 
```

### 进程池化

```python
import concurrent.futures
 
# 定义进程要执行的函数
def worker(index):
    print(f"Process {index} is starting")
    print(f"Process {index} is done")
 
# 使用进程池创建多进程
#  max_workers=3 表示创建一个最大容量为 3 的进程池，即同时可以运行的进程数量不会超过 3 个。
with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
# 提交多个进程任务 创建一个包含 5 个任务的列表，每个任务都会执行 worker 函数，传递不同的索引值作为参数。
    # 方式 1
    futures = [executor.submit(worker, i) for i in range(5)]
    
    ### 多种方法访问futures的结果，有不同的操作逻辑 ###
    
    ### 生产者消费者模式感觉更适用于第二种方式 ###
    
   for future in future.as_completed()
 	# 方式 2
   	results = executor.map(worker,[1,2,3])
 
# 等待所有进程完成
concurrent.futures.wait(futures)
print("All processes are done")
```

## asyncio 协程

asyncio是一个python的库，提供协程相关操作，协程适用于高并发操作的网络应用，该库是在**单线程**情况下实现的cpu和io同时进行，一个线程中可以包含多个协程，最多甚至可以有万个。但是有很多的库并不完成支持协程，且协程的实现也有一定的困难，例如request就不支持异步操作，但有专门的库aiohttp来支持request/response的异步。

协程实现代码更加复杂，适合超多任务同时执行。

通过 async 标识来实现异步函数 

```python
import asyncio
import aiohttp
 
 
# 异步函数，用于从 URL 获取内容
async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()
 
 
# 主函数，用于并发发送多个 HTTP 请求
async def main():
    urls = ['https://www.csdn.net/', 'https://www.baidu.com',]
 
    # 使用 aiohttp 创建异步会话
    async with aiohttp.ClientSession() as session:
        # 创建异步任务列表，每个任务会调用 fetch_url 函数，传递不同的 URL
        tasks = [fetch_url(session, url) for url in urls]
 
        # 并发执行所有异步任务，并等待结果
        results = await asyncio.gather(*tasks)
 
        # 打印每个 URL 的内容长度
        for url, result in zip(urls, results):
            print(f"Content from {url}: {len(result)} bytes")
 
 
# 创建并运行事件循环
loop = asyncio.get_event_loop()
loop.run_until_complete(main())  # 运行主函数并等待其完成
loop.close()  # 关闭事件循环
```

## 锁

python 提供lock原语保护并发下共享资源的访问,可以通过threading和multiprocessing库导入

```python
lock = Lock()
with lock：
	# do something
```

## 信号量

python也提供信号量机制来控制并发度和共享资源保护，在asyncio库中支持

```python

```

## 进程间通信

python通过queue来实现进程间通信，从而实现``生产者-消费者``模式。使用queue来实现pipeline。

例如爬虫中生产者为网页下载，消费者是网页解析，使用queue存储下载好的网页。

在函数定义中传参，把pipeline传入作为消息队列。

## python并发编程的应用

### web

使用并发加速 api/file/db的访问，这些都是 io 操作，适用于线程池，可以把这些任务提交到线程池中来实现并发。

多进程和多线程的使用方式有所不同，多进程的多个进程之间环境是完全隔离的，需要先初始化后才能使用。
