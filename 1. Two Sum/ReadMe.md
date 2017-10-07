
## 题目
给你一个列表nums和一个数字target，如果列表里面有两个数之和等于target，则返回两个数字的下坐标，这两个数不能为同一个数。(假设总会有这两个数)

1.py	时间复杂度O(n^2)
2.py	时间复杂度O(n)


### python有关的知识要点：

#### 1. 列表生成器

[表达式 for 变量 in 列表]  或   [表达式 for 变量 in 列表 if 条件]
[x**2 for x in range(5)]        [0, 1, 4, 9, 16]

#### 2. enumerate()
```python
for index, num in  enumerate(nums):
    pass
```