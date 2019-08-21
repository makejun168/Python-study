# 水鲜花数

# 找出100~999之间的所有水仙花数
# 水仙花数是各位立方和等于这个数本身的数
# 如: 153 = 1**3 + 5**3 + 3**3

for a in range(100, 999):
    low = a % 10
    middle = a // 10 % 10
    high = a // 100
    if a == low ** 3 + middle ** 3 + high ** 3:
        print(a)
