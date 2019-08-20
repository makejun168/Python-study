# Craps赌博游戏
# 玩家可以下注任意数量
# 玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
# 如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
# 玩家再次要色子 如果摇出7点 庄家胜
# 如果摇出第一次摇的点数 玩家胜
# 否则游戏继续 玩家继续摇色子
# 玩家进入游戏时有1000元的赌注 全部输光游戏结束

from random import randint

money = 1000
while money > 0:
    # 打印出你的资产数
    print('你的总资产为:', money)
    while True:
        debt = int(input('请下注: '))
        if debt > money or debt <= 0:
                break

        first = randint(1, 6) + randint(1, 6)
        print('玩家的第一次点数是%d' % first)
        if first == 7 or first == 11:
            print('玩家胜')
            money += debt
            print('玩家的现金是%d' % money)
        elif first == 2 or first == 3 or first == 12:
            print('庄家胜')
            money -= debt
            print('玩家的现金是%d' % money)
        else:
            second = randint(1, 6) + randint(1, 6)
            print('玩家的第二次点数是%d' % second)
            if second == 7:
                print('庄家胜')
                money -= debt
                print('玩家的现金是%d' % money)
            elif first == second:
                print('玩家胜')
                money += debt
                print('玩家的现金是%d' % money)
            else:
                print('退出')
                break

print('你破产了, 游戏结束!')
