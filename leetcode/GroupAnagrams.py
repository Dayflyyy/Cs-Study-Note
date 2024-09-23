# 思路：计算每个字符串字符的哈希值和，相等

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hm = {}
        for s in strs:
            if (s):
                sum = 0
                for i in range(0, len(s)):
                    sum += hash(s[i])
                # 考虑到有可能会出现hash值加和相等，再加一个该字符串中字典序最小的字母作为校验值。
                # min 不可以迭代空字符串，增加条件判断是否为空
                sum += hash(min(s))
                if (sum in hm):
                    hm[sum].append(s)
                else:
                    hm[sum] = [s]
            else:
                hm[0] = [s]
        output = []
        for v in hm.values():
            output.append(v)

        print(output)
        return output


sol = Solution()
sol.groupAnagrams(["",""])
sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
sol.groupAnagrams([""])
sol.groupAnagrams(["a"])
sol.groupAnagrams(["cab", "tin", "pew", "duh", "may", "ill", "buy", "bar", "max", "doc"])


# 题解思路：将字符串按字典序排序

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hm = {}
        for s in strs:
            # 将字符串排序后的结果作为键
            sorted_s = ''.join(sorted(s))
            if sorted_s in hm:
                hm[sorted_s].append(s)
            else:
                hm[sorted_s] = [s]

        output = []
        for v in hm.values():
            output.append(v)

        print(output)
        return output


sol = Solution()
sol.groupAnagrams(["", ""])


sol.groupAnagrams(["",""])
sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
sol.groupAnagrams([""])
sol.groupAnagrams(["a"])
sol.groupAnagrams(["cab", "tin", "pew", "duh", "may", "ill", "buy", "bar", "max", "doc"])


"""
当然可以！以下是关于 Python 中 `str.join` 方法和 `sorted` 方法的详细介绍：

### `str.join` 方法

#### 功能
`str.join` 方法用于将一个可迭代对象（如列表、元组等）中的所有元素连接成一个字符串，并在每个元素之间插入指定的分隔符。

#### 语法
```python
separator.join(iterable)
```

- `separator`：用于分隔的字符串。
- `iterable`：可迭代对象，其元素必须是字符串类型。

#### 示例
```python
# 连接列表中的字符串，用逗号分隔
words = ["Hello", "world", "Python"]
result = ", ".join(words)
print(result)  # 输出：Hello, world, Python

# 连接元组中的字符串，用空格分隔
words_tuple = ("join", "method", "example")
result = " ".join(words_tuple)
print(result)  # 输出：join method example
```

### `sorted` 方法

#### 功能
`sorted` 方法返回一个排序后的新列表，原列表不变。该方法可以对任何可迭代对象进行排序，如列表、元组、字符串等。

#### 语法
```python
sorted(iterable, key=None, reverse=False)
```

- `iterable`：要排序的可迭代对象。
- `key`（可选）：一个函数，如果提供了此参数，将对每个元素调用一次该函数，并按照函数返回值排序。
- `reverse`（可选）：一个布尔值，如果设为 `True`，将按降序排序，默认值为 `False`。

#### 示例
```python
# 对列表进行排序
numbers = [3, 1, 4, 1, 5, 9]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # 输出：[1, 1, 3, 4, 5, 9]

# 对字符串进行排序
string = "hello"
sorted_string = sorted(string)
print(sorted_string)  # 输出：['e', 'h', 'l', 'l', 'o']

# 使用 key 参数排序
words = ["apple", "banana", "cherry"]
sorted_words = sorted(words, key=len)
print(sorted_words)  # 输出：['apple', 'cherry', 'banana']

# 按降序排序
numbers = [3, 1, 4, 1, 5, 9]
sorted_numbers_desc = sorted(numbers, reverse=True)
print(sorted_numbers_desc)  # 输出：[9, 5, 4, 3, 1, 1]
```

### 综合示例

结合 `str.join` 和 `sorted` 方法的示例：

```python
# 将字符串按字符排序，然后连接成一个新的字符串
original_string = "python"
sorted_chars = sorted(original_string)
sorted_string = "".join(sorted_chars)
print(sorted_string)  # 输出：hnopty
```

在你的代码中，使用 `''.join(sorted(s))` 是为了将字符串 `s` 按字符排序并连接成一个新的字符串，这样可以用于分组异位词。

"""