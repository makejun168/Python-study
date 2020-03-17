"""
面向对象版本的猜数字游戏

"""
from random import randint

class guessNum(object):
    def __init__(self, max, min):
        self._max = max
        self._min = min
        self._answer = None

    def guess(self, your_answer):
        self._answer = randint(self._min, self._max)
        if your_answer > self._answer:
            print('大了一点')
            return False
        elif your_answer < self._answer:
            print('小了一点')
            return False
        else:
            print('恭喜你猜中了')
            return True

    def start(self):
        game_over = False
        while not game_over:
            your_answer = int(input('请输入你猜的数字:'))
            print(your_answer)
            game_over = self.guess(self, your_answer)


def main():
    gm = guessNum(100, 1)
    gm.start()

if __name__ == '__main__':
    main()


