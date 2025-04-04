import os
import common.base as Base

def main():
    print("hello world")


def add(a: int, b: int) -> int:
    return a + b
"""
这是多行注释
"""
class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    def print_user(self):
        print("name:", self.name, "age:", self.age)

# main run
if __name__ == '__main__':
    main()
    user = User("zhangsan", 18)
    user.print_user()
    cpu_nums = os.cpu_count()
    print("cpu count:", cpu_nums)
    root : Base.TreeNode = Base.TreeNode(1)

