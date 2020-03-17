def _foo():
    print('student');

# 定义学生类 可以传入 Object 对象
class Student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    # 通过传入的对应
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 使用驼峰命名字法
    def watchTV(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看爱情动作片.' % self.name)

# 定义一个主进程方法
def main():
    # 对象实例化
    # 传入了 两个参数 kobe & age
    stu1 = Student('James', 20)
    stu1.study('数学')
    stu1.watchTV()

# 执行主进程
if __name__ == '__main__':
    main();