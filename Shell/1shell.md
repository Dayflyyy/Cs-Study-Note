# shell

### 基础的bash命令

+ 查看文件内容

```bash
cat filename
```

+ 进入到具体目录

```bash
cd /path
# 一般来说使用/正斜杠
cd .. #进入到上一级目录
```

+ 目录

```bash
mkdir directory #新建文件夹

rm -rf D:/SRTP/2024-SEU-SRTP #移除特定路径下的特定目录
ls #查看当前目录下的文件
mv directory1/ /path/to/directory2/
#这将`directory1/`移动到`/path/to/directory2/`目录中。
```

+ 文件

```bash
cp /path/file.txt 
touch file.txt #新建文本文件
./filename #执行该文件//需要管理员权限
mv file1.txt /path/to/directory/
mv oldfile.txt newfile.txt
#这将`oldfile.txt`重命名为`newfile.txt`。

```

+ 打印或输出文本

```bash
echo hello #输出hello
foo=bar
echo "$foo"
# 打印 bar
echo '$foo'
# 打印 $foo
echo hello > file.txt
echo hello > /path/file.txt
#将文本输入到file.txt 文件中

cat filename | grep "pattern"
grep -i "pattern" filename

```

+ 查看程序

```bash
man [程序名]
```
