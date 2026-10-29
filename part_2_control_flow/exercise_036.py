"""
题目 036: 健壮的文件读取函数

要求:
编写一个名为 `robust_read_file` 的函数，它接受一个文件路径 `filepath`。
1. 使用 `try...except` 块来处理 `FileNotFoundError`。如果文件不存在，函数应返回 `None`。
2. 如果文件存在，函数应读取并返回其内容。
3. 使用 `finally` 块来确保无论文件是否存在，都会打印一条消息 `"File operation finished."`。

提示:
这是将错误处理与文件操作结合的绝佳实践。
"""

def robust_read_file(filepath):
    # 在这里写下你的代码
    try:
        with open(filepath,'r',encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("文件读取错误")
        return None
    finally:
        print("File operation finished.")


print(robust_read_file("test_file.txt"))
print(robust_read_file("test_file1.txt"))