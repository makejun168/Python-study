"""
输入一个正整数判断它是不是素数
素数指的是 只有1和它本身两个因数的自然数
"""


from math import sqrt

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))

print(end)

is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)