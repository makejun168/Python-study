# 百块百鸡的问题

a = 5
b = 3
c = 1 / 3

for x in range(0, 100):
    for y in range(0, 100):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print((x, y, z))
