def main():
    print(fib_recursive_memoized_top_down(8))
    print(fib_recursive_bottom_up(8))
    print(fib_simply_looping(8))
    print(fib_recursive_slow_top_down(8))


def fib_recursive_slow_top_down(n):
    if n<= 2:
        return 1
    return fib_recursive_slow_top_down(n-1) + fib_recursive_slow_top_down(n-2)


def fib_recursive_memoized_top_down(n, memo=dict()):
    if memo.get(n) is not None:
        return memo.get(n)
    if n<= 2:
        return 1
    memo[n] = fib_recursive_memoized_top_down(n-1, memo) + fib_recursive_memoized_top_down(n-2, memo)
    return memo.get(n)


def fib_recursive_bottom_up(n, cur=2, vals=[1,1]):
    if n <= 2:
        return 1
    elif cur == n:
        return vals[1]
    else:
        vals[0], vals[1] = vals[1], vals[0]+vals[1]
        return fib_recursive_bottom_up(n, cur+1, vals=vals)


def fib_simply_looping(n):
    if n<=2:
        return 1
    cur, prev = 1, 1
    for i in range(3, n+1):
        prev, cur = cur, prev+cur
    return cur

if __name__ == '__main__':
    main()
