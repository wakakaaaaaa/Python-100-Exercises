"""
题目 020: 检查列表中的元素是否都唯一

要求:
编写一个名为 `are_all_unique` 的函数，它接受一个列表 `items` 作为参数。如果列表中的所有元素都是唯一的，则返回 `True`，否则返回 `False`。

提示:
集合 (`set`) 是一种只包含唯一元素的数据结构。你可以将列表转换为集合，然后比较它们的长度。
"""

def are_all_unique(items):
    # 在这里写下你的代码
    new_items = set(items)
    if len(items) == len(new_items):
        return True
    else:
        return False
    pass

print(are_all_unique([1,2,3]))
print(are_all_unique([1,2,3,5]))
print(are_all_unique([1,2,3,1]))
print(are_all_unique([1,2,3,'1']))
print(are_all_unique([]))

