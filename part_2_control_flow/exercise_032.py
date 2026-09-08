"""
题目 032: 为类添加构造函数

要求:
修改 `Person` 类，为其添加一个 `__init__` 方法（构造函数）。
这个方法应该接受 `name` 和 `age` 两个参数，并将它们分别存为实例的属性 `self.name` 和 `self.age`。
"""


class Person:
    # 在这里写下你的代码
    def __init__(self, age, name):
        self.name = name
        self.age = age


p1 = Person(30, "Alice")
print(Person(p1.age, p1.name))
print(p1.age, p1.name)
