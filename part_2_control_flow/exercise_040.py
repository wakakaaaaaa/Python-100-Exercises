"""
题目 040: 查找列表中的第二大数

要求:
编写一个名为 `find_second_largest` 的函数，它接受一个数字列表 `numbers` 作为参数，
并返回其中第二大的数字。如果列表元素少于2个，或者所有元素都相同，可以返回 `None`。

提示:
一个直接的方法是先对**列表去重**并排序，然后取倒数第二个元素。
注意处理列表长度不足的边界情况。
"""
from pydantic_core.core_schema import none_schema


def find_second_largest(numbers):
    # 在这里写下你的代码
    list0 = list(set(numbers))
    if len(list0)<2:
        return None
    else:
        list0_max = max(list0)
        list0.remove(list0_max)
        second_largest = max(list0)
    return second_largest
    pass
find_second_largest([1,2,2,3,4,4])
find_second_largest([2,2,2,2,2,2])
find_second_largest([ ])


