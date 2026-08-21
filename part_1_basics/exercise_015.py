"""
题目 015: 使用函数式API处理列表

要求:
1. 编写一个名为 `square_list(numbers)` 的函数，使用 `map` 和一个 `lambda` 函数，返回一个新列表，其中每个数字都是原列表数字的平方。
2. 编写一个名为 `filter_odd_numbers(numbers)` 的函数，使用 `filter` 和一个 `lambda` 函数，返回一个只包含奇数的新列表。
3. 编写一个名为 `sum_with_reduce(numbers)` 的函数，使用 `functools.reduce` 和一个 `lambda` 函数，计算列表中所有数字的和。

提示:
对于第3点，你可能需要 `from functools import reduce`。
"""
from functools import reduce

def square_list(numbers):
    # 在这里写下你的代码
    new_list = list(map(lambda x: x*x, numbers))
    pass
    return new_list

def filter_odd_numbers(numbers):
    # 在这里写下你的代码
    filtered_list = list(filter(lambda x : x % 2 != 0,numbers))
    pass
    return filtered_list

def sum_with_reduce(numbers):
    # 在这里写下你的代码
    reduced_list = reduce(lambda a,b :a + b,numbers,0)#这个需要有一个最初的值，要不然当可迭代对象为空时会出现报错的
    pass
    return reduced_list

print(square_list([1,2,3,4]))
print(filter_odd_numbers([1,2,3,4]))
print(sum_with_reduce([1,2,3,4]))