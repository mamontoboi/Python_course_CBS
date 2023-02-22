# def mean_value(number):
#     sum = 0
#     cnt = 0
#     for i in range(number):
#         a = int(input("Value:"))
#         sum += a
#         cnt += 1
#     print(sum, sum / cnt)
#
# def main():
#     mean_value(3)
#
# if __name__ == '__main__':
#     main()


def prt(left, center, right, second_right):
    for i in (left, center, right, second_right):
        print(i)


prt('three', 'four', 'tszy', 'jedyn')

prt('three', 'four', second_right='tszy', right='jedyn')