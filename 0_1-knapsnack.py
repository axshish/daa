def knapsack(weights, values, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    print("\nFilling DP table step by step:")
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]
            
            print(f"dp[{i}][{w}] = {dp[i][w]} (Item {i-1}, Weight {weights[i-1]}, Value {values[i-1]})")
    
    print("\nFinal DP table:")
    for row in dp:
        print(row)

    selected_items = []
    total_value = dp[n][capacity]
    w = capacity

    print("\nTracing back to find included items:")
    for i in range(n, 0, -1):
        if total_value <= 0:
            break
        if total_value != dp[i - 1][w]:
            selected_items.append(i - 1)
            print(f"Item {i-1} included (Weight {weights[i-1]}, Value {values[i-1]})")
            total_value -= values[i - 1]
            w -= weights[i - 1]

    selected_items.reverse()
    return dp[n][capacity], selected_items

weights = list(map(int, input("Enter weights: ").split()))
values = list(map(int, input("Enter values: ").split()))
capacity = int(input("Enter capacity of knapsack: "))

if len(weights) != len(values):
    print("Error: Number of weights must match number of values.")
else:
    max_value, selected_items = knapsack(weights, values, capacity)
    print("\nMaximum value in knapsack:", max_value)
    print("Items included (0-indexed):", selected_items)