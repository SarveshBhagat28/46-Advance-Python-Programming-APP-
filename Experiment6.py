# Bottom-Up Approach
def knapsack_bottom_up(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Top-Down Approach
def knapsack_top_down(weights, values, n, capacity, memo):
    if n == 0 or capacity == 0:
        return 0

    if (n, capacity) in memo:
        return memo[(n, capacity)]

    if weights[n - 1] <= capacity:
        memo[(n, capacity)] = max(
            values[n - 1] + knapsack_top_down(
                weights, values, n - 1,
                capacity - weights[n - 1], memo
            ),
            knapsack_top_down(weights, values, n - 1, capacity, memo)
        )
    else:
        memo[(n, capacity)] = knapsack_top_down(
            weights, values, n - 1, capacity, memo
        )

    return memo[(n, capacity)]


# Example
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

print("Bottom-Up:", knapsack_bottom_up(weights, values, capacity))

memo = {}
print("Top-Down:", knapsack_top_down(
    weights, values, len(weights), capacity, memo
))
