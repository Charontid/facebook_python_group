def main():
    pi_approximation = Leibniz_pi(5000)
    for approx in pi_approximation:
        print(approx)


def Leibniz_pi(n):
    x = 0
    for i in range(n):
        x +=  (-1)**(i % 2) * 4 / (2 * i + 1)
        yield x


if __name__ == '__main__':
    main()
