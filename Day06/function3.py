# - 数学相关: abs / divmod / pow / round / min / max / sum
# - 序列相关: len / range / next / filter / map / sorted / slice / reversed
# - 类型转换: chr / ord / str / bool / int / float / complex / bin / oct / hex
# - 数据结构: dict / list / set / tuple
# - 其他函数: all / any / id / input / open / print / type


def myfilter(mystr):
    return len(mystr) == 6

print(chr(0x9a6c))
print(hex(ord('马')))
print(abs(-1.2345))
print(round(-1.2345))
print(pow(1.2345, 5))


fruits = ['orange', 'peach', 'durian', 'watermelon']
print(fruits[slice(1, 3)])
fruits2 = list(filter(myfilter, fruits))
print(fruits)
print(fruits2)
print(len('orange'))
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(arr[slice(5)])
print([0, 1, 2, 3, 4, 5, 6, 7, 8, 9][slice(5)])

arr2 = list(fruits)
print(arr2)

test1 = [{'a': 1}]

aTuple = (123, 'xyz', 'zara', 'abc')
aList = list(aTuple)

print("列表元素 : ", aList)

while True:
    try:
        # 获得下一个值:
        x = next(test1)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
