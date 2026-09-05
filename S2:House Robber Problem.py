houses = list(map(int, input("Enter the amount in each house: ").split()))

n = len(houses)

if n == 0:
    print("Maximum amount:", 0)
elif n == 1:
    print("Maximum amount:", houses[0])
else:
    dp = [0] * n

    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])

    print("Maximum possible amount:", dp[n - 1])
