"""
用while循环实现1~100之间的偶数求和
"""

res = 0
num = 2

while num <= 100:
    res += num
    num += 2

print(res)
