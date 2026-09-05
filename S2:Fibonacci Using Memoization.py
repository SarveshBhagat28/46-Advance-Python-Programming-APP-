
def fibonacci(n, memo):
    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

N = int(input("Enter N: "))
memo = {}
sequence = []

for i in range(N):
    sequence.append(fibonacci(i, memo))

print("Fibonacci Sequence:", sequence)
