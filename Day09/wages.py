"""
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""
from abc import ABCMeta, abstractmethod


class Person(object, metaclass=ABCMeta):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        pass


class Manager(Person):
    def get_salary(self):
        return 15000


class Programmer(Person):
    def __init__(self, name, working_hours=0):
        # 继承父类的方法
        super().__init__(name)
        self._working_hour = working_hours

    @property
    def working_hour(self):
        return self._working_hours

    @working_hour.setter
    def working_hour(self, working_hour):
        self._working_hour = working_hour if working_hour > 0 else 0

    def get_salary(self):
        return 150 * self._working_hour


class Sales(Person):
    def __init__(self, name, sales=0):
        super().__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return self.sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0

    def get_salary(self):
        return 1200 + 0.05 * self._sales


def main():
    total = 0
    emps = [
        Manager('刘备'), Programmer('诸葛亮'),
        # Manager('曹操'), Sales('荀彧'),
        # Sales('吕布'), Programmer('张辽'),
        # Programmer('赵云')
    ]
    for emp in emps:
        if isinstance(emp, Programmer):
            emp.working_hour = int(input('请输入%s本月工作时间: ' % emp.name))
        elif isinstance(emp, Sales):
            emp.sales = float(input('请输入%s本月销售额: ' % emp.name))
        # 同样是接收get_salary这个消息但是不同的员工表现出了不同的行为(多态)
        print('%s本月工资为: ￥%s元' %
              (emp.name, emp.get_salary()))
        total += emp.get_salary()
        print('总共工资支出：￥%s元' % total)


if __name__ == '__main__':
    main()

