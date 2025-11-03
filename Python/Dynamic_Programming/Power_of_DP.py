dp = [-1] * 110


def fib(n):
    if n <= 1:
        return 1

    # if memoized value present then fetch it
    if dp[n] != -1:
        return dp[n]

    # set 'dp' elements for memoization
    dp[n] = fib(n - 1) + fib(n - 2)
    return dp[n]


for i in range(1, 105):
    print(f"Fibonacci of {i} is = {fib(i)}")
