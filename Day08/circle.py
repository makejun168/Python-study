"""
练习
修一个游泳池 半径(以米为单位)在程序运行时输入 游泳池外修一条3米宽的过道
过道的外侧修一圈围墙 已知过道的造价为25元每平米 围墙的造价为32.5元每米
输出围墙和过道的总造价分别是多少钱(精确到小数点后2位)

"""
# 需要使用到数学模型
import math


class Circle(object):
    # 游泳池的半径是 xxx
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    # 设置 radius 的限制
    @radius.setter
    def radius(self, radius):
        self._radius = radius if radius > 0 else 0

    # 获取整个游泳池的周长 2 pi r
    @property
    def perimeter(self):
        return 2 * math.pi * self._radius

    # 获取整个游泳池的面积 pi r * r
    @property
    def area(self):
        return math.pi * self._radius * self._radius


if __name__ == '__main__':
    radius = float(input('请输入游泳池的半径: '))
    # 小圆
    small = Circle(radius)
    # 大圆
    big = Circle(radius + 3)
    print('大圆形的周长是：%.1f' % big.perimeter)
    print('小圆形的周长是：%.1f' % small.perimeter)
    print('围墙的造价为: ￥%.1f元' % (big.perimeter))
    print('过道的造价为: ￥%.1f元' % ((big.area - small.area)))
