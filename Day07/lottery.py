# 输出列表中的双色球号码

from random import randrange, randint, sample


def display(balls):
    for index, ball in enumerate(balls):  # enumerate 创建序列
        if index == len(balls) - 1:  # 为了显示特别号码
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


def random_select():
    # 1 - 33之间选择 一组数字

    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    # 随机选择6个序列
    selected_balls = sample(red_balls, 6)
    # 快速排序
    selected_balls.sort()
    print(selected_balls)
    # 1，15之间选择一个特别数字
    selected_balls.append(randint(1, 16))
    return selected_balls


def main():
    n = int(input('机选几注: '))
    for _ in range(n):
        # random_select()
        display(random_select())


if __name__ == '__main__':
    main()


