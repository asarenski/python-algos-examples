def fib(n, memo = {0:0,1:1}):
    if n in memo:
        return memo[n]
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

print(fib(35))

def fibDP(n):
    if n == 0 or n == 1:
        return n
    nMinusOne = 1
    nMinusTwo = 0
    for i in range(2, n):
        temp = nMinusOne
        nMinusOne = nMinusOne + nMinusTwo
        nMinusTwo = temp
    return nMinusOne + nMinusTwo

print(fibDP(35))

    