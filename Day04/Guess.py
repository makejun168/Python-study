# 猜数字游戏
# 可以猜猜看到底数字是多少 1 - 100

import random

answer = random.randint(1, 100)
counter = 0

while True:
    counter += 1
    number = int(input('请输入你要猜的数字: '))
    if number == answer:
        print('你猜对了真棒')
        break
    elif number > answer:
        print('数字大了')
    else:
        print('数字小了了')

print('总共猜了%d次' % counter)

if counter > 7:
    print('你的智商好像不是太够用哟')
