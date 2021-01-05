class HiddenInt(int):
    def __init__(self, num):
        int().__init__(num)

    def __str__(self):
        tmp = str(self.real)
        if tmp[0] == '-':
            mask = '*' * (len(tmp)-4)
            sign = '-'
        else:
            mask = '*' * (len(tmp)-3)
            sign = ''
        tail = tmp[-3:]
        return ''.join([sign, mask, tail])


if __name__ == '__main__':
    x = HiddenInt(1234567890)
    print(x)
    y = HiddenInt(1000000010)
    z = HiddenInt(x+y)
    print(z)
    print(repr(z))

    negative = HiddenInt(-1234567890)
    print(negative)
