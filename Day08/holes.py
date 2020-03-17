def main():
    names = ['Make', 'Kobe', '666']
    subjs = ['语文', '数学', '英语']
    scores = [[]] * names.__len__()
    for row, name in enumerate(names):
        scores[row] = [0] * subjs.__len__()
        print('请输入%s的成绩' % name)
        for col, subj in enumerate(subjs):
            # float 浮点数设置
            scores[row][col] = float(input(subj + ': '))
    print(scores)


# 输出的内容 都是 最后一位的一致内容
# [[20.0, 20.0, 20.0], [20.0, 20.0, 20.0], [20.0, 20.0, 20.0], [20.0, 20.0, 20.0], [20.0, 20.0, 20.0]]

if __name__ == '__main__':
    main()
