## 题目
给定两个数字，数字以列表的形式给出，要求计算这两个数字的和，并把结果也用列表的形式返回。


### python有关的知识要点：

#### 1. divmod(a, b)
divmod(a,b)方法返回的是a//b（除法取整）以及a对b的余数
返回结果类型为tuple

#### 2. 关于ListNode
LeetCode里面用的是自定义的ListNode格式的数据。自己测试的时候需要下面的方式生成
```python
def Create_ListNode(nums):
    _next = None
    for num in nums[::-1]:
        l1 = ListNode(num)
        l1.next = _next
        _next = l1
    return l1
Create_ListNode([2,4,3])
```