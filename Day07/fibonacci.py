"""
生成斐波拉切数列

"""

def main():
    f = [1 , 1]
    for i in range(2, 20):
        f += [f[i - 1] + f[i - 2]]
        # f.append(f[i - 1] + f[i - 2])
    for val in f:
        print(val, end=' ')


if __name__ == '__main__':
    main()
